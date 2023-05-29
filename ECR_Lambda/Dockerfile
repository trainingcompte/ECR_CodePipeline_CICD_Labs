FROM public.ecr.aws/lambda/python:3.7

RUN pip3 install opencv-python==4.6.0.66

#Copy python file 
COPY lambda_function.py /var/task/ 
# Run the application:
CMD ["lambda_function.lambda_handler"]
#-----------------------------------------------------

