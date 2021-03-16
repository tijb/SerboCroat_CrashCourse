segments:
	mkdir ./segments
	python3 ./scripts/SplitFiles.py ./raw/all_verbs.csv 20 Verbs
	python3 ./scripts/SplitFiles.py ./raw/all_phrases.csv 20 Phrases
	mv *.csv ./segments/
iphone: segments
	mkdir ./iphone
	python3 ./scripts/AnkikunFormat.py ./segments
	mv *\ iPhone.csv ./iphone/
zip_iphone: iphone
	cd ./iphone && zip ../AnkiKun-iPhone.zip ./* && cd ..
zip_segments: segments
	cd ./segments && zip ../Segmented.zip ./* && cd ..
clean:
	rm -rf ./segments
	rm -rf ./iphone
	rm -f *.zip
