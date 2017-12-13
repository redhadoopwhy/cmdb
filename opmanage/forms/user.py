# -*- coding: utf-8 -*-
# 2017-12-13
# by why

from django import forms

from opmanage.models import User_info

def checkusername_exit(username):
    """
        检查用户名是否存在
    :param username:
    :return:
    """
    check_userexit_status = User_info.objects.filter(username=username).count()
    if check_userexit_status == 1:
        return True
    else:
        return False

class AddUserForm(forms.Form):
    cmdb_auth = ((1, "user"),(10,"host"))
    email = forms.CharField()
    password = forms.CharField()
    auth = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple(),choices=cmdb_auth)
    jumper = forms.CharField()
    vpn = forms.CharField()
    phone = forms.CharField()
    department = forms.CharField()
    zabbix = forms.CharField()
    kibana = forms.CharField()

    # def clean(self):
    #     cleaned_data = super(AddUserForm, self).clean()
    #     username = cleaned_data.get('username')
    #     if checkusername_exit(username) == False:
    #         self.add_error('username', '用户名不存在')


class DelUserForm(forms.Form):
    username = forms.CharField()
    manager_password = forms.CharField()

    def clean(self):
        cleaned_data = super(DelUserForm, self).clean()
        username = cleaned_data.get('username')
        if checkusername_exit(username) == False:
            self.add_error('username', '用户名不存在')

class UpdataUserForm(forms.Form):
    manager_password = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(required=False)
    auth = forms.CharField(required=False)
    jumper = forms.CharField(required=False)
    vpn = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    department = forms.CharField(required=False)
    zabbix = forms.CharField(required=False)
    kibana = forms.CharField(required=False)


class GetUserForm(forms.Form):
    username = forms.CharField()