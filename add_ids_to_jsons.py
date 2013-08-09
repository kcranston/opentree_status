# reads status jsons
# extracts studyID and adds as _id field
# so that can be import into couchdb
# assumes 1. want to import all .json files
import sys
import os
import json
import glob

def usage() :
    print "Usage: add_study_ids.py source_directory target_directory"

# crappy command-line parameter parsing
source_dir=sys.argv[1]
print "source files in",source_dir
target_dir=sys.argv[2]
if os.path.isdir(target_dir):
    print "writing files to",target_dir
else:
    os.mkdir(target_dir)
    print "creating",target_dir

# get the list of files to import
filelist=os.listdir(source_dir)
jsons={}
for f in filelist:
    if f.endswith(".json"):
        infile = source_dir+"/"+f
        outfile = target_dir+"/"+f
        contents = json.load(open(infile,'r'))
        studyId = contents['study_info']['ot:studyId']
        contents['_id'] = studyId
        json.dump(contents,open(outfile,'w'))
        print infile,outfile,studyId
        jsons[studyId]=infile
        
    else:
        print "skipping file ",f

    
