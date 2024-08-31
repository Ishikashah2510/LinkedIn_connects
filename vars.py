excel_path = 'company_role_details.xlsx'
cmd_ctrl = 'ctrl' # cmd if using on mac
message = "Hi {}, I saw there was an opening for a {} at {} & I am looking to get a referral. I have 1+ years of exp, along with multiple projects in ML, DL and LLMs along with proficiency in Python, Tensorflow, AWS. I look forward to connecting with you and sharing my resume. Thanks!"
shift_opt = 'shift' # option if using on mac


geo_region = 103644278
sleep_time = 5
gap_time = 2
prompt = """
{}
--------------------------------------------------
I want 10 indian names out of the list above.
follow the following rules while giving me an answer:
1. the names have to definitely be indians.
2. I dont want any other extra characters, your answer should include only the names from the list.
3. no ordering is needed, no  bullet points either.
4. Give it as a python list.
5. you have to give me maximum 10 names, can be lesser than 10 names, its okay. 10 or lesser names is okay. 
6. The names have to be from my provided list only. dont add any other names.
"""
