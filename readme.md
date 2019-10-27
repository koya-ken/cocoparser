## required package

```
conda install numpy
conda install -c conda-forge rapidjson
conda install -c anaconda msgpack-python
```

## analyze.py

```
python .\analyze2.py .\person_keypoints_val2017.msgpack
```

## analyze2.py

```
python .\analyze2.py .\person_keypoints_val2017.msgpack
```

## filter_imagecount.py

```
python .\filter_imagecount.py .\person_keypoints_val2017.msgpack -c 100 -o .\tmp\val_image_100.json
```

```
python .\filter_imagecount.py .\person_keypoints_val2017.msgpack -c 100 -s 200 -o .\tmp\val_image_200.json
```

