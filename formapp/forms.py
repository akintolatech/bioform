from django import forms


class StudentForm(forms.Form):
    # Student Information
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    student_class = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Class'}))
    squadron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Squadron'}))
    svc_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'SVC No:'}))
    admission_date = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Admission Date'}))
    blood_group = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Blood Group'}))
    tribe = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Tribe'}))
    state_of_origin = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'State of Origin'}))
    lga = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'L.G.A'}))
    date_of_birth = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Date of Birth'}))
    place_of_birth = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Place of Birth'}))
    religion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Religion'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    hobbies = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Hobbies'}))

    # Guardian/Parent Information
    guardian_parent_name = forms.CharField(max_length=100,
                                           widget=forms.TextInput(attrs={'placeholder': 'Guardian/Parent Name'}))
    relationship = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Relationship'}))
    occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Occupation'}))
    guardian_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    guardian_state_of_origin = forms.CharField(max_length=50,
                                               widget=forms.TextInput(attrs={'placeholder': 'State of Origin'}))
    telephone_no = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Telephone No:'}))
    next_of_kin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name of Next of Kin'}))
