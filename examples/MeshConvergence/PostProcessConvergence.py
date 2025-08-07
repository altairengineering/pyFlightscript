import pathlib, os, pdb, json
import pandas as pd
import matplotlib.pyplot as plt

######### DONT EDIT
cwd = str(pathlib.Path(__file__).parent.resolve()) + '\\'
uTable = []
vTable = []

def load_config():
    """Load configuration from config.json file"""
    config_path = os.path.join(cwd, "config.json")
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def write_sweep_csv(output, config):
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
                    aoa_runs = int((config['aoaStop'] - config['aoaStart']) / config['aoaDelta'] )
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
    return

def plot_df(df):
    """
    Creates plots for each force coefficient vs AoA for all U values.
    Saves plots in a 'plots' folder.
    """
    import os
    
    # Create plots directory if it doesn't exist
    plots_dir = os.path.join(cwd, "plots")
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    
    # Force coefficients to plot (excluding mesh info and flow conditions)
    force_coefficients = ['Cx', 'Cy', 'Cz', 'CL', 'CDi', 'CD0', 'Cl', 'Cm', 'Cn']
    
    # Get unique U values for different mesh densities
    u_values = sorted(df['Mesh_U'].unique())
    
    # Create a plot for each force coefficient
    for force in force_coefficients:
        plt.figure(figsize=(10, 6))
        
        # Plot each U value as a separate line
        for u_val in u_values:
            df_u = df[df['Mesh_U'] == u_val]
            plt.plot(df_u['AoA'], df_u[force], 'o-', label=f'U={u_val}', linewidth=2, markersize=6)
        
        plt.xlabel('Angle of Attack (degrees)', fontfamily='Times New Roman')
        plt.ylabel(force, fontfamily='Times New Roman')
        plt.title(f'{force} vs Angle of Attack - Mesh Convergence Study', fontfamily='Times New Roman')
        plt.legend(prop={'family': 'Times New Roman'})
        
        # Set x-axis ticks to increment by 1.0
        plt.xticks(fontfamily='Times New Roman')
        plt.yticks(fontfamily='Times New Roman')
        
        # Save the plot
        plot_filename = f'AoA_vs_{force}.png'
        plot_path = os.path.join(plots_dir, plot_filename)
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure to free memory
        
        print(f"Saved plot: {plot_filename}")
    
    print(f"All plots saved in: {plots_dir}")
    return


#Analyse Results & Calculate Convergence
def analyze_results():
    with open(cwd + "ConvergenceResults.csv", "r") as results:
        #Skip the first 2 lines
        line = results.readline()
        line = results.readline()
        line = results.readline()
        line = results.readline()
        #now do stuff
        print(results.readline())

    results.close()

    # read the file with one header row
    df = pd.read_csv(cwd + "ConvergenceResults.csv", header=1)

    # Create plots for all force coefficients
    plot_df(df)

    return

#main function
if __name__ == "__main__":
    # Load configuration from config.json
    config = load_config()
    
    uVal = config['uStart']
    vVal = config['vStart']
    uStop = config['uStart'] + (config['uInterval'] * config['uInts'])
    vStop = config['vStart'] + (config['vInterval'] * config['vInts'])
    
    if config['runU']:
        while uVal <= uStop:
            uTable.append(uVal)
            uVal += config['uInterval']

    if config['runV']:
        while vVal <= vStop:
            vTable.append(vVal)
            vVal += config['vInterval']

    with open(cwd + "ConvergenceResults.csv", "w") as output:
        write_sweep_csv(output, config)
        output.close()
    
    analyze_results()
