import pathlib, os
import shutil, pdb
import pandas as pd
import matplotlib.pyplot as plt
import json
import pyFlightscript as pyfs

######### DONT EDIT
cwd = str(pathlib.Path(__file__).parent.resolve()) + '\\'

# Load configuration from JSON file
config_path = os.path.join(cwd, "config.json")
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

# Extract configuration variables
refFrame = config['refFrame']
runU = config['runU']
uStart = config['uStart']
uInterval = config['uInterval']
uInts = config['uInts']
runV = config['runV']
vStart = config['vStart']
vInterval = config['vInterval']
vInts = config['vInts']
aoaStart = config['aoaStart']
aoaStop = config['aoaStop']
aoaDelta = config['aoaDelta']

uTable = []
vTable = []


def import_run_export(path, xval, UV):
    meshes_dir = os.path.join(path, "meshes")
    ccsPath = os.path.join(meshes_dir, "Analysis" + UV + str(xval) + ".csv")
    pyfs.ccs_import(ccsPath)
    # pyfs.solver_uninitialize()
    pyfs.analysis.set_vorticity_drag_boundaries(-1)
    # pyfs.set_solver.set_axial_separation_boundaries([1])
    # pyfs.wake.physics(auto_trail_edges=True)
    pyfs.initialize_solver("INCOMPRESSIBLE", -1, "DEFAULT", "MIRROR", 1, "DISABLE", "ENABLE", 1.0)
    pyfs.change_scene_to("PLOTS")
    pyfs.execute_solver_sweeper(path + "results\\"+ "Analysis" + UV + str(xval) + ".txt", 
                   angle_of_attack='ENABLE',  
                   angle_of_attack_start=aoaStart, 
                   angle_of_attack_stop=aoaStop, 
                   angle_of_attack_delta=aoaDelta,
                   export_surface_data_per_step='DISABLE', 
                   clear_solution_after_each_run='ENABLE',
                   reference_velocity_equals_freestream='ENABLE',
                   append_to_existing_sweep='DISABLE')
                   
    # pyfs.post_surf.create_new_surface_section(offset=-2.4892, surfaces=[1])
    # pyfs.post_surf.update_all_surface_sections()
    # pyfs.plots.set_plot_type('SECTIONS_CP')
    # filename = 'section_cp_' + UV + str(xval) + '.txt'
    # pyfs.plots.save_plot_to_file(filename)
    # pyfs.post_surf.delete_surface_section(1)
    
    return

#Write & Run the FS script
def writerun_fs_script(path):
    fsexe_path = r'C:\Users\denriquez\Documents\CodingDojo\Altair FlightStream\FlightStream\test\builds\Chimera-Windows.exe' #specify file path to FS exe
    pyfs.hard_reset() # (optional) clear lines from local memory, delete existing script.txt
    pyfs.open_fsm(fsm_filepath=os.path.join(path, "base.fsm"))

    # pyfs.surface_clearall()

    # import, run, and export each ccs file
    for x in uTable:
        import_run_export(path, x, UV="U")
            
    for x in vTable:
        import_run_export(path, x, UV="V")
            
    pyfs.close_flightstream()
    pyfs.write_to_file() # now write script_out.txt
    pyfs.execute_fsm_script(fsexe_path=fsexe_path) # execute the script in headless FS
    return

def write_sweep_csv(output):
    output.write("SWEEP RESULTS,\n")
    output.write("Mesh_U,Mesh_V,AoA,Beta,Flow,Cx,Cy,Cz,CL,CDi,CD0,Cl,Cm,Cn,\n")
    searchPhrase = "AOA"
    
    #Store sweep data
    sweepData = []
    dataIndex = 0
    for u in uTable:
        fpath = os.path.join(cwd, "results", "AnalysisU" + str(u) + ".txt")
        # Check if the file exists
        if os.path.exists(fpath):
            with open(fpath, "r") as results:
                #Search for the data results
                for num,line in enumerate(results, 1):
                    if searchPhrase in line:
                        print("Found line, " + str(num))
                        dataIndex = num + 1
                        break
                #If we found data, read it to file
                if dataIndex > 0:
                    results.seek(0)
                    data = results.readlines()
                    aoa_runs = int((aoaStop - aoaStart) / aoaDelta )
                    for aoax in range(0, aoa_runs+1): 
                        sweepData.append(str(u)+',Default,' + data[dataIndex + aoax])
                    
                #Close the file
                results.close()

    for x in sweepData:
        output.write(x)
    sweepData.clear()

    dataIndex = 0
    for v in vTable:
        fpath = os.path.join(cwd, "results", "AnalysisV" + str(v) + ".txt")
        
        if os.path.exists(fpath):
            with open(fpath, "r") as results:
                #Search for the data results
                for num,line in enumerate(results, 1):
                    if searchPhrase in line:
                        print("Found line, " + str(num))
                        dataIndex = num + 1
                        break
                #If we found data, read it to file
                if dataIndex > 0:
                    results.seek(0)
                    data = results.readlines()
                    sweepData.append('Default,'+str(v)+',' + data[dataIndex])
                    sweepData.append('Default,'+str(v)+',' + data[dataIndex+1])
                #Close the file
                results.close()

    for x in sweepData:
        output.write(x)
    sweepData.clear()


#Write CCS files for the script
def write_ccs_files(uVal, input, UV="U"):
    GR = 1.1 # growth rate input

    # Ensure meshes directory exists
    meshes_dir = cwd + "meshes"
    if not os.path.exists(meshes_dir):
        pathlib.Path(meshes_dir).mkdir(parents=True, exist_ok=True)

    #read input file, write corrected output
    name = "Analysis" + UV + str(uVal) + ".csv"
    path = os.path.join(meshes_dir, name)
    with open(path, "w") as output:
        input.seek(0)
        text = input.readlines()
        for line in text:
            #iterate through each line
             index = line.find("Mesh_" + UV)
             if index>=0:
                 
                 GRstring = ";1;1;1\n"
                 if GR > 1.0:
                     GRstring = ";3;" + str(GR) + ";2\n"
                     
                 writeline = "Mesh_"  + UV + ";" + str(uVal) + GRstring
                 output.write(writeline)
             else:
                output.write(line)
        output.close()                 
    return

def run_convergence_study():
    """Run the full mesh convergence study"""
    # delete the folder results and all files within if needed
    if not os.path.exists(cwd + "results"):
        pathlib.Path(cwd + "results").mkdir(parents=True, exist_ok=True)
    
    # Create meshes directory if it doesn't exist
    meshes_dir = cwd + "meshes"
    if not os.path.exists(meshes_dir):
        pathlib.Path(meshes_dir).mkdir(parents=True, exist_ok=True)

    # Initialize mesh value tables
    uVal = uStart
    vVal = vStart
    uStop = uStart + (uInterval * uInts)
    vStop = vStart + (vInterval * vInts)

    with open(cwd + "Analysis.csv", "r") as read:
        if runU:
            while uVal <= uStop:
                uTable.append(uVal)
                write_ccs_files(uVal, read, UV="U")
                uVal += uInterval

        if runV:
            while vVal <= vStop:
                vTable.append(vVal)
                write_ccs_files(vVal, read, UV="V")
                vVal += vInterval

        # Write and run the FlightStream script
        writerun_fs_script(cwd)
        read.close()

    return

#main function  
if __name__ == '__main__':
    print("Starting mesh convergence study...")
    print(f"Configuration loaded from {config_path}")
    print(f"U mesh range: {uStart} to {uStart + (uInterval * uInts)} with interval {uInterval}")
    if runV:
        print(f"V mesh range: {vStart} to {vStart + (vInterval * vInts)} with interval {vInterval}")
    print(f"AoA range: {aoaStart} to {aoaStop} with interval {aoaDelta}")
    
    # Run the convergence study
    run_convergence_study()
    print("Convergence study completed.")
    
