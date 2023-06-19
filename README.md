# Purpose
Build an ML flask service to predict height by weight using continuous delivery. This project uses Cloud9 to develop and test feature, it uses CodeBuild to trace code changes and publish a docker image to ECR. Then, AppRunner subscribes the latest version of that docker image and deploy to production. 

## Requirements
- Python 3.9
- Flask
- Jupyter Notebook
- Pandas
- Scikit-learn

> Note: Jupyter Notebook, Pandas, and Scikit-learn are not required for production. They are only used for training model.


## How to use
### Train model
Open `Baseball_Predictions_Export_Model.ipynb` in Jupyter Notebook and modify the code to generate a new model. Save the model file in `./models/model.joblib`

### Deploy change to prod

Every `git push` will trigger a CodeBuild job to build a new docker image and push to ECR. Then, AppRunner will subscribe the latest version of that docker image and deploy to production. You just need to wait the deployment to finish.

### Test service
- Test homepage: `curl https://j4fmgsh4pz.us-east-1.awsapprunner.com`
- Test prediction: `curl -X POST -H "Content-Type: application/json" -d '{"Weight": 200}' https://j4fmgsh4pz.us-east-1.awsapprunner.com/predict`

Remember to modify the URL to your own AppRunner URL.

