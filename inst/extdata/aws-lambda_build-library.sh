# taken from 'how to use pandas in aws lambda' (available online:
# https://www.gcptutorials.com/post/how-to-use-pandas-in-aws-lambda)
mkdir python
pip install pandas -t python
zip -r pandas_pyarrow.zip python
rm -rf python