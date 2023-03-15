#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Pré-Start Functions.

@author: AIR Centre
"""

### Import Libraries ############################################################################
import os

#################################################################################################
def input_checker():
    """
    This function checks inputs to confirm if they are correct.
    Input: User inputs based on User_Inputs.py
    Output: inputs_flag - Can be 0 if at least one input fails or 1 if all inputs pass. 
    """
    from configs.User_Inputs import search, service, roi, nrt_sensing_period, sensing_period
    from configs.User_Inputs import stream_processing
    from configs.User_Inputs import download, download_options
    from configs.User_Inputs import atmospheric_correction
    from configs.User_Inputs import masking, masking_options
    from configs.User_Inputs import classification, classification_options
    from configs.User_Inputs import delete
    from configs.User_Inputs import s2l1c_products_folder, ac_products_folder, masked_products_folder, classification_products_folder
    
    inputs_flag = 1
    if isinstance(search, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'search' is not boolean.")

    if isinstance(service, str):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'service' is not string.")

    if isinstance(roi, dict):
        if len(roi) == 2:
            if (roi["type"]=="Polygon") and isinstance(roi["coordinates"], list):
                inputs_flag = inputs_flag*1
            else:
                inputs_flag = inputs_flag*0
                print("'roi' has incorrect values.")
        else:
            inputs_flag = inputs_flag*0
            print("'roi' does not have dimension 2.")
    else:
        inputs_flag = inputs_flag*0
        print("'roi' is not dictionary.")

    if isinstance(nrt_sensing_period, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'nrt_sensing_period' is not boolean.")

    if isinstance(sensing_period, tuple):
        if len(sensing_period) == 2:
            if isinstance(sensing_period[0], str) and isinstance(sensing_period[1], str):
                inputs_flag = inputs_flag*1
            else:
                inputs_flag = inputs_flag*0
                print("'sensing_period' values are not strings.")
        else:
            inputs_flag = inputs_flag*0
            print("'sensing_period' does not have dimension 2.")
    else:
        inputs_flag = inputs_flag*0
        print("'sensing_period' is not tuple.")

    if isinstance(stream_processing, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'stream_processing' is not boolean.")

    if isinstance(download, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'download' is not boolean.")

    if isinstance(download_options, dict):
        if len(download_options) == 1:
            if isinstance(download_options["lta_attempts"], int):
                inputs_flag = inputs_flag*1
            else:
                inputs_flag = inputs_flag*0
                print("'download_options' has incorrect values.")
        else:
            inputs_flag = inputs_flag*0
            print("'download_options' does not have dimension 1.")
    else:
        inputs_flag = inputs_flag*0
        print("'download_options' is not dictionary.")

    if isinstance(atmospheric_correction, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'atmospheric_correction' is not boolean.")

    if isinstance(masking, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'masking' is not boolean.")

    if isinstance(masking_options, dict):
        if len(masking_options) == 9:
            if isinstance(masking_options["use_existing_ESAwc"], bool) and isinstance(masking_options["land_buffer"], int) and\
                isinstance(masking_options["threshold_values"], list) and isinstance(masking_options["dilation_values"], list) and\
                isinstance(masking_options["cloud_mask"], bool) and isinstance(masking_options["cloud_mask_threshold"], float) and\
                isinstance(masking_options["cloud_mask_average"], int) and isinstance(masking_options["cloud_mask_dilation"], int):
                inputs_flag = inputs_flag*1
            else:
                inputs_flag = inputs_flag*0
                print("'masking_options' has incorrect values.")
        else:
            inputs_flag = inputs_flag*0
            print("'masking_options' does not have dimension 9.")
    else:
        inputs_flag = inputs_flag*0
        print("'masking_options' is not dictionary.")

    if isinstance(classification, bool):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'classification' is not boolean.")

    if isinstance(classification_options, dict):
        if len(classification_options) == 10:
            if isinstance(classification_options["split_and_mosaic"], bool) and isinstance(classification_options["classification_probabilities"], bool) and\
                isinstance(classification_options["ml_algorithm"], str) and isinstance(classification_options["model_path"], str) and\
                isinstance(classification_options["n_classes"], int) and isinstance(classification_options["features"], tuple) and\
                isinstance(classification_options["n_hchannels"], int) and isinstance(classification_options["features_mean"], list) and\
                isinstance(classification_options["features_std"], list):
                inputs_flag = inputs_flag*1
            else:
                inputs_flag = inputs_flag*0
                print("'classification_options' has incorrect values.")
        else:
            inputs_flag = inputs_flag*0
            print("'classification_options' does not have dimension 10.")
    else:
        inputs_flag = inputs_flag*0
        print("'classification_options' is not dictionary.")

    if isinstance(delete, dict):
        if len(delete) == 3:
            if isinstance(delete["original_products"], bool) and isinstance(delete["some_intermediate"], bool) and\
                isinstance(delete["all_intermediate"], bool):
                inputs_flag = inputs_flag*1
            else:
                inputs_flag = inputs_flag*0
                print("'delete' has incorrect values.")
        else:
            inputs_flag = inputs_flag*0
            print("'delete' does not have dimension 3.")
    else:
        inputs_flag = inputs_flag*0
        print("'delete' is not dictionary.")

    if isinstance(s2l1c_products_folder, str):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'s2l1c_products_folder' is not string.")

    if isinstance(ac_products_folder, str):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'ac_products_folder' is not string.")

    if isinstance(masked_products_folder, str):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'masked_products_folder' is not string.")

    if isinstance(classification_products_folder, str):
        inputs_flag = inputs_flag*1
    else:
        inputs_flag = inputs_flag*0
        print("'classification_products_folder' is not string.")
    
    return inputs_flag

#################################################################################################
def ScriptOutput2List(ScriptOutput, ListOfOutputs):
    """
    This function adds the script's output to a list.
    Input:  ScriptOutput - Script's output as string. 
            ListOfOutputs - List, empty or not, with the string outputs from the script.
    Output: ListOfOutputs - The ScriptOutput added to the previous ListOfOutputs.
    """
    ListOfOutputs.append(ScriptOutput)
    print(ScriptOutput)
    
    return ListOfOutputs

#################################################################################################
def ScriptOutputs2LogFile(ListOfAllOutputs, FolderName):
    """
    This function saves the script's outputs as a text log file on a folder.
    Input: ListOfAllOutputs - List with all string outputs from the script.
           FolderName - Name (string) of the folder to save the text log file.
    Output: Folder with text log file with all outputs.
    """
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    LogFileName = os.path.join(FolderName, "LogFile.txt")
    LogFile = open(LogFileName,"w") 
    LogFile.writelines(Line + "\n" for Line in ListOfAllOutputs)
    LogFile.close()

################################################################################################
def CloneModulesFromGitHub(SaveFolder):
    """
    This function clones FeLS and ACOLITE from GitHub and extracts on a folder.
    Input: SaveFolder - Name (string) of the folder to save the modules.
    Output: Modules extracted on folder.
    """
    FeLSfolder = os.path.join(SaveFolder, "fetchLandsatSentinelFromGoogleCloud-master")
    ACOLITEfolder = os.path.join(SaveFolder, "acolite-main")
    
    if not os.path.exists(FeLSfolder):
       print("\nCloning FeLS from GitHub...") 
       FeLSclone = "git clone https://github.com/EmanuelCastanho/fetchLandsatSentinelFromGoogleCloud.git " + FeLSfolder
       os.system(FeLSclone)
       print("Done.\n")

    if not os.path.exists(ACOLITEfolder):
       print("Cloning ACOLITE from GitHub...") 
       ACOLITEclone = "git clone https://github.com/acolite/acolite.git " + ACOLITEfolder
       os.system(ACOLITEclone)
       print("Done.\n")

################################################################################################