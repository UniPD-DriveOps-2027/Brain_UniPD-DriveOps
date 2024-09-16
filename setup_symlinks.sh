#!/bin/bash
# Create symbolic links for shared files and directories between simulator_2024 and ws_2024

SHARED_DIR_SIM=../shared_code
SHARED_DIR_WS_SMART=../../../shared_code
SHARED_DIR_WS_CONTROL=../../../../shared_code

SIMULATOR_DIR=simulator_2024
WS_SMART_DIR=ws_2024/src/smart
WS_CONTROL_DIR=ws_2024/src/control/src

# List of shared files for the smart directory
SMART_FILES=(
    "automobile_data_interface.py"
    "automobile_data_pi.py"
    "automobile_data_simulator.py"
    "automobile_ekf.py"
    "brain.py"
    "controller3.py"
    "controllerAG.py"
    "controllerSP.py"
    "detection.py"
    "environmental_data_simulator.py"
    "gps_angles.pkl"
    "helper_functions.py"
    "highway_dict.pkl"
    "main_brain.py"
    "names_and_constants.py"
    "obstacle2.py"
    "parkman.py"
    "path_planning4.py"
    "rc_brain.py"
    "stopline.py"
)

# Create symbolic links for files in the smart directory
for file in "${SMART_FILES[@]}"; do
    ln -sf $SHARED_DIR_SIM/$file $SIMULATOR_DIR/$file
    ln -sf $SHARED_DIR_WS_SMART/$file $WS_SMART_DIR/$file
done

# List of specific files for the control/src directory
CONTROL_FILES=(
    "automobile_data_interface.py"
    "automobile_data_pi.py"
    "automobile_ekf.py"
    "helper_functions.py"
)

# Create symbolic links for only the specific control/src files
for file in "${CONTROL_FILES[@]}"; do
    ln -sf $SHARED_DIR_WS_CONTROL/$file $WS_CONTROL_DIR/$file
done

# Handle full directories (data and models)
DATA_DIR_SIM="$SIMULATOR_DIR/data"
DATA_DIR_SMART="$WS_SMART_DIR/data"
MODELS_DIR_SIM="$SIMULATOR_DIR/models"
MODELS_DIR_SMART="$WS_SMART_DIR/models"


# Create symbolic links for data and models directories
ln -sf $SHARED_DIR_SIM/data $DATA_DIR_SIM
ln -sf $SHARED_DIR_WS_SMART/data $DATA_DIR_SMART
ln -sf $SHARED_DIR_SIM/models $MODELS_DIR_SIM
ln -sf $SHARED_DIR_WS_SMART/models $MODELS_DIR_SMART

echo "Symbolic links created"
