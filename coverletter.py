import os 

kwargs = {
    'date':input("Today's date : "),
    'job':input('Job title : '),
    'companyName':input('Company Name : '),
    'address' : [x.strip() for x in input('Company Address (street,city,state,zip): ').split(',',1)]
}



coverletter = """
{date}

{companyName}
{address[0]}
{address[1]}

To {companyName}, 

    My name is Matthew Kang and I am a recent graduate of UCSD with a B.S in Machine Learning and a minor in Data Science. Currently I am employed as a coding instructor for an educational technology company called Hackingtons, and prior, I was an instructional assistant at UCSD. 

    I am applying to {companyName}'s position of {job} that I found through my alumni network. My experience in university and in employment has given me a skillset that aligns with the needs of the role at hand. My education at UCSD left me with a very practical skillset for industry. I have 5 years of experience programming in Python and using Pythonic libraries such as Pandas, Matplotlib, Seaborn, SK-Learn, PyTorch,Dask, and many more. I also have multiple upper division statistics courses under my belt which means I have experience with statistical concepts like distributions, correlation coefficients, and Bayesian Statistics. I have experience with SQL and Relational Database Management Systems like PostgreSQL and SQLite. I also have experience dash boarding with software like Tableau and PowerBI.

    In my work with UCSD, I Designed a data pipeline that cleans CSVs and handles null values. It can parse files up to 5 milllion rows in size in under 1 minute. I also analyzed the Chicago Taxicab dataset, which contains 25 million entries. Partitioning the 30GB csv file was done with DASK. I also created a taskMaster application platform with Flask, a python framework. It saves potential users 30 hours every month. 

    My experience in teaching, at both UCSD and Hackingtons, has taught me how to manage small teams and to inspire success. Furthermore, it has made me incredibly adept at explaining high level concepts in ways that anyone can understand. 

Thank you for your time. I look forward to speaking with you more in person about this role, and what I can do for {companyName}.

Matthew Kang
925-216-6150
me@mattkang.com

""".format(**kwargs)

filename = '/Users/matthewkang/Documents/jobstuff/COVER_LETTERS/'+kwargs['companyName']+'CoverLetter.txt'
filenamePDF = '/Users/matthewkang/Desktop/'+kwargs['companyName']+'CoverLetter.pdf'

output_file =  open(filename,'w+')
output_file.writelines(coverletter)
output_file.close()

os.system(f'enscript -B -f "Helvetica12" --word-wrap {filename} --margin=72:72:72:72 --output=- | ps2pdf - > {filenamePDF}')

