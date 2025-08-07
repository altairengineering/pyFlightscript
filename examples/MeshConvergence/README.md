# Mesh Convergence Analyzer

A Python tool for automated mesh convergence studies in FlightStream. This tool systematically varies mesh density parameters and analyzes aerodynamic force convergence to help determine optimal mesh settings.

## Overview

The Mesh Convergence Analyzer automates the process of:
- Running multiple FlightStream simulations with varying mesh densities
- Extracting aerodynamic coefficients from simulation results
- Generating convergence plots and analysis
- Determining optimal mesh parameters for accurate CFD results

## Project Structure

```
MeshConvergenceAnalyzer/
├── config.json              # Configuration file with mesh parameters and run settings
├── base.fsm                  # Base FlightStream model file
├── RunConvergenceStudy.py    # Main script to execute convergence study
├── PostProcessConvergence.py # Post-processing and plotting script
├── constants.py              # Legacy constants file (replaced by config.json)
├── meshes/                   # Directory containing mesh analysis CSV files
├── results/                  # Directory containing FlightStream output files
├── plots/                    # Generated convergence plots (created automatically)
├── ConvergenceResults.csv    # Compiled results from all simulations
└── README.md                # This file
```

## Quick Start

### 1. Configure the Study

Edit `config.json` with your desired mesh parameters:

```json
{
  "refFrame": "1",
  "runU": true,      // Enable U-direction mesh convergence
  "uStart": 80,      // Starting U mesh density
  "uInterval": 20,   // U mesh increment
  "uInts": 9,        // Number of U intervals (final = uStart + uInterval * uInts)
  
  "runV": false,     // Enable V-direction mesh convergence  
  "vStart": 80,      // Starting V mesh density
  "vInterval": 30,   // V mesh increment
  "vInts": 9,        // Number of V intervals
  
  "aoaStart": 2,     // Starting angle of attack (degrees)
  "aoaStop": 10,     // Ending angle of attack (degrees)
  "aoaDelta": 2      // AoA increment (degrees)
}
```

**Recommended Workflow:**
1. First run U-direction convergence with V held constant (`runU: true`, `runV: false`)
2. Once converged U value is found, run V-direction convergence (`runU: false`, `runV: true`)

### 2. Prepare FlightStream Model

Edit `base.fsm` to reflect your desired FlightStream configuration:
- Geometry setup
- Flow conditions
- Boundary conditions
- Solver settings

### 3. Customize Simulation Steps (Optional)

Modify the `import_run_export` function in `RunConvergenceStudy.py` to customize:
- FlightStream import/export procedures
- Simulation parameters
- Output file handling

### 4. Run the Convergence Study

```bash
python RunConvergenceStudy.py
```

This will:
- Create multiple mesh configurations based on config.json
- Run FlightStream simulations for each configuration
- Save results to the `results/` directory
- Generate mesh analysis files in `meshes/` directory

### 5. Post-Process and Generate Plots

```bash
python PostProcessConvergence.py
```

This will:
- Compile all simulation results into `ConvergenceResults.csv`
- Generate convergence plots for each force coefficient vs. AoA
- Save plots in the `plots/` directory with Times New Roman fonts

## Output Files

### ConvergenceResults.csv
Contains compiled aerodynamic coefficients for all mesh configurations:
- **Mesh_U, Mesh_V**: Mesh density parameters
- **AoA**: Angle of attack
- **Cx, Cy, Cz**: Force coefficients in body axes
- **CL, CDi, CD0**: Lift and drag coefficients
- **Cl, Cm, Cn**: Moment coefficients

### Generated Plots
The tool automatically generates convergence plots:
- `AoA_vs_CL.png` - Lift coefficient convergence
- `AoA_vs_CDi.png` - Induced drag convergence
- `AoA_vs_CD0.png` - Zero-lift drag convergence
- And plots for all other force coefficients

Each plot shows multiple lines representing different mesh densities, allowing visual assessment of mesh convergence.

## Interpreting Results

1. **Mesh Convergence**: Look for curves that converge to similar values as mesh density increases
2. **Optimal Mesh**: Choose the mesh density where further refinement produces minimal change in results
3. **Force Coefficient Trends**: Verify that aerodynamic trends are physically reasonable

## Configuration Tips

- Start with coarser meshes and progressively refine
- Use smaller intervals (`uInterval`, `vInterval`) for finer convergence studies
- Adjust AoA range (`aoaStart`, `aoaStop`, `aoaDelta`) based on your flight envelope
- Monitor computational time vs. accuracy trade-offs

## Requirements

- Python 3.x
- pandas
- matplotlib
- FlightStream installation
- Sufficient disk space for multiple simulation results

## Troubleshooting

- Ensure FlightStream paths are correctly configured
- Check that `base.fsm` file is valid and accessible
- Verify sufficient system resources for multiple simulations
- Review `script_out.txt` for detailed execution logs
