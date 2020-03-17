from django.shortcuts import render, redirect

from .models import (createAccountTable, dropTableAccount, deleteAllRowsFromAccount, insertIntoAccount, getAllAccounts)

# Create your views here.


def accountSetup(request):
    # dropTableAccount()
    # createAccountTable()
    all_Accounts = getAllAccounts()
    print(all_Accounts)
    print("Account View's accountSetup() function called.")
    return redirect("/")

def create_account_view(request):
    print("CREATE ACCOUNT VIEW")
    if request.method == "POST":
        print(request.POST["username"])
        print(request.POST["password"])
        insertIntoAccount(request.POST["username"], request.POST["password"])
        redirect("/")
    return render(request, "create_account_form.html", {})
