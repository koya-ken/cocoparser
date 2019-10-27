## required package

```
conda install numpy
conda install -c conda-forge rapidjson
conda install -c anaconda msgpack-python
```

## analyze_plot.py

```
python .\analyze_plot.py .\person_keypoints_val2017.msgpack
```

## analyze_single.py

```
python .\analyze_single.py .\person_keypoints_val2017.msgpack
```

## analyze_diff.py

```
python .\analyze_diff.py .\tmp\val_image_100.json .\tmp\merged.json 
```


## filter_imagecount.py

```
python .\filter_imagecount.py .\person_keypoints_val2017.msgpack -c 100 -o .\tmp\val_image_100.json
```

```
python .\filter_imagecount.py .\person_keypoints_val2017.msgpack -c 100 -s 200 -o .\tmp\val_image_200.json
```

## filter_annotationcount.py

```
python .\filter_annotationcount.py .\person_keypoints_val2017.msgpack -c 100 -o .\tmp\val_annotation_100.json
```

```
python .\filter_annotationcount.py .\person_keypoints_val2017.msgpack -c 100 -s 200 -o .\tmp\val_annotation_200.json
```
## merge.py

```
python .\merge.py .\tmp\val_image_100.json .\tmp\val_image_200.json -o .\tmp\merged.json
```

## filter.py

```
python .\filter.py .\tmp\merged.json -f 'num_keypoints > 15' -o .\tmp\over_keypoints_15.json
```

```
python .\filter.py .\person_keypoints_val2017.json -f 'annotation_count < 5, width > 200 , height > 200' -o .\tmp\val_over_annotation_0.json
```

## dumpid.py

```
python .\dumpid.py .\tmp\merged.json -o .\tmp\image_ids.txt
```

```
python .\dumpid.py .\tmp\merged.json -o .\tmp\annotation_ids.txt --annotation
```

```
python .\dumpid.py .\tmp\merged.json -o - --annotation
```