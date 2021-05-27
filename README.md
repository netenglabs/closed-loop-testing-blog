# closed-loop-testing-blog

This is the Repo for the closed loop network change testing blog post available [here]() and on [Medium](). 

To use the code and repo in this repository, you must follow the instructions in the post, as well as install pytest to run the test files.

To run:

* The Batfish pre-approval test: ```pytest test_pre_approval.py```
* The Suzieq deployment pre-test: ```pytest test_deploy_pre.py```
* The Suzieq deployment post-test: Edit the suzieq-cfg.yml file to change the data-directory name from parquet-pre-deploy to parquet-post-deploy and run ```pytest test_deploy_post.py```
* The Batfish pre-approval test with the incorrect IP address: Edit the test_pre_approval.py file and change the SNAPSHOT_DIR value from './add-leaf03/' to './add-leaf03-bug' and run ```pytest test_pre_approval.py```
