from azureml.core import Workspace, Experiment, Run

# Load workspace from Azure ML Studio
workspace = Workspace.from_config()

# Retrieve the experiment containing the finished job
experiment_name = 'diabetes-classification-production'
experiment = Experiment(workspace, experiment_name)

# Get the latest completed run from the experiment
latest_run = next(experiment.get_runs(status='Completed'))

# Assuming your job outputs a model file, you can retrieve it like this
model_file_path = latest_run.get_file_names()

# Register the model
model = Model.register(workspace=workspace,
                       model_path=model_file_path,
                       model_name='my-model',
                       tags={'area': 'classification'},
                       description='Description of your model')

print('Model registered:', model.name, model.id)
