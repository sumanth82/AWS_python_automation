'''

Lambda Programming Model -

Handler files and functions - Entry Point for Lambda invocations 
Events - Incoming Data passed to passed to lambda function when triggered
Context - provides methods and properties that provide info about the invocation, function and execution env 
Logging
Exceptions


'''
'''

Handler Format:

<function_name>.lambda_handler

<function_name> --> Name of the python file lambda is interacting with. 
lambda_handler --> Name of the function indise the python file 

event --> data passed to the lambda_handler function 

context --> Get runtime info like request_id etc.. 

