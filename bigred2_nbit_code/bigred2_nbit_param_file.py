import numpy as np 
import bigred2_mkPCPcommand_files

experimental_parameters = {
    'num_threads': 512,#736
    'q1_list': np.linspace(0.0, 0.5, 20),
    'q2_list': [1024], #17
    'qsub_nodes': 16,#16,23
    'qsub_ppn': 32,
    'qsub_time': '01:30:00',
    'qsub_cpu_type': 'cpu',
    'worker_file': 'bigred2_nbitworker.py',
    'command_prefix': 'c1_e10_N1k_rsig0.3_gain2.0_ws1.0_lrb-0.1_urb1.0_dl4-5_mu-fp',
    'q1': 'mu',
    'q2': 'num_trials',
    'num_reservoir_samplings': 50,
    'num_validation_trials': 256,
    'fixed_point_analysis': True,
    'nbit_task_parameters': {
    'loop_unique_input': True,
    'recall_task': True,
    'distractor_value': 0,
    'cue_value':1,
    'sequence_dimension': 4,
    'start_time': 0,
    'sequence_length': 5,
    'distraction_duration': 1000,
    'input_fraction': 0.3,
    'input_gain': 2.0,
    'num_trials': 1024,
    'neuron_type': 'sigmoid',
    'neuron_pars': {'c':1., 'e': 10},
    'output_neuron_type': 'heaviside',
    'output_neuron_pars': {'threshold': 0.5},
    'N': 1000,
    'mu': 0.1,
    'k': 7, 
    'maxk': 7,
    'homok': None,
    'com_size': None, 
    'minc':10, 
    'maxc':10, 
    'deg_exp':1.0, 
    'temp_dir_ID':0,
    'full_path': '/N/u/njrodrig/BigRed2/topology_of_function/',#'/nobackup/njrodrig/topology_of_function/',
    'reservoir_weight_scale': 1.0,
    'input_weight_bounds': (1.0,1.0),#(1.0, 1.0),
    'lower_reservoir_bound': -0.1,
    'upper_reservoir_bound': 1.0
    }
}

bigred2_mkPCPcommand_files.run_qsub(experimental_parameters)