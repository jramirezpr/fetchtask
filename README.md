predictor of receipts
model trained with time_series.ipynb
(if you want to replicatethe training, easiest is to run in google colab on cpu)
the trained model is saved as multimodelfile2
docker image of http api is saved on docker hub as

 https://hub.docker.com/r/jramirezpr1/myimage

you can either do 

```
docker pull jramirezpr1/myimage
```

or build the image from the dockerfile. Then, launch the container as:

```
docker run -d --name fetchcontainer -p 80:80 -p 8000:8000 jramirezpr1/myimage
```
This launches a uvicorn server with a FastAPI interface.you can see the docs at http://127.0.0.1/docs
You will need three things: last_available_date is the last date of info
available in format yyyy-mm-dd.

receipts_for_that_day gives the number of receipts for the last_available_date

starting_prediction_date is the date when we want our30 day prediction
e.g. doing a get to http://127.0.0.1/prediction/2022-08-01/8000000/2022-08-02
returns 
```
'{"schema":{"fields":[{"name":"index","type":"integer"},{"name":"datep","type":"string"},{"name":"receipt","type":"number"}],"primaryKey":["index"],"pandas_version":"1.4.0"},"data":[{"index":0,"datep":"2022-08-02","receipt":11409083.4982020035},{"index":1,"datep":"2022-08-03","receipt":11519515.8836424462},{"index":2,"datep":"2022-08-04","receipt":12073323.3783807568},{"index":3,"datep":"2022-08-05","receipt":11640370.9425932691},{"index":4,"datep":"2022-08-06","receipt":11670789.517657103},{"index":5,"datep":"2022-08-07","receipt":11397153.7861244101},{"index":6,"datep":"2022-08-08","receipt":11579103.6628139205},{"index":7,"datep":"2022-08-09","receipt":11591647.8990926184},{"index":8,"datep":"2022-08-10","receipt":11603347.5374856964},{"index":9,"datep":"2022-08-11","receipt":11594469.3780778535},{"index":10,"datep":"2022-08-12","receipt":11621099.568056047},{"index":11,"datep":"2022-08-13","receipt":11599233.4322000183},{"index":12,"datep":"2022-08-14","receipt":11624217.3088603225},{"index":13,"datep":"2022-08-15","receipt":11632004.9488348309},{"index":14,"datep":"2022-08-16","receipt":11617062.6511864047},{"index":15,"datep":"2022-08-17","receipt":11628881.0553307272},{"index":16,"datep":"2022-08-18","receipt":11655557.4837803636},{"index":17,"datep":"2022-08-19","receipt":11645737.0290714316},{"index":18,"datep":"2022-08-20","receipt":11663213.4932676218},{"index":19,"datep":"2022-08-21","receipt":11670778.5173755903},{"index":20,"datep":"2022-08-22","receipt":11654287.6038247421},{"index":21,"datep":"2022-08-23","receipt":11667165.7639032528},{"index":22,"datep":"2022-08-24","receipt":11694075.0627191439},{"index":23,"datep":"2022-08-25","receipt":11684630.4820361324},{"index":24,"datep":"2022-08-26","receipt":11701874.8216478638},{"index":25,"datep":"2022-08-27","receipt":11709437.7948558889},{"index":26,"datep":"2022-08-28","receipt":11692620.4153232016},{"index":27,"datep":"2022-08-29","receipt":11705602.0526261106},{"index":28,"datep":"2022-08-30","receipt":11732753.1711898297},{"index":29,"datep":"2022-08-31","receipt":11723116.5516939703}]}'
``` 
