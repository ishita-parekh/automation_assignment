import base
import signup
import login
import workorder

base.set_up()  # set_up function

signup.signup()  # signup function

login_status = login.login()  # login function

if login_status:
    print("User logged in successfully")
    #  Workorder scenarios
    workorder.create()
    workorder.search()
    workorder.filter_opt()
else:
    print("User entered incorrect email or password")

base.tear_down()  # tear_down function
