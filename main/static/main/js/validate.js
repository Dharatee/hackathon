function checklogin()
{
	var usrname=document.getElementById('userName').value;
	var pwrd=document.getElementById('password').value;
	if(usrname=="")
	{
		window.alert("Please! Enter your Username");
		return false;
	}
	if(pwrd=="")
	{
		window.alert("Please! Enter your Password");
		return false;
	}
}
function checksignupuser()
{
	var name=document.getElementById('name').value;
	var pwrd1=document.getElementById('password1').value;
	var rpwrd=document.getElementById('password2').value;
	var address=document.getElementById('address').value;
	var bloodgroup=document.getElementById('bloodGroup').value;
	var usertype=document.getElementById('userType').value;
	var email = document.getElementById('email');
	var filter = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	var cntct=document.getElementById('contact').value;

	if (name=="")
	{
		window.alert("Please! Enter your Name");
		return false;
	}
	if (email!="")
	{	
		if (!filter.test(email.value)) 
		{
	    alert('Please! Enter your Email Or Provide a valid email address');
	    email.focus;
	    return false;
		}
	}
	if (cntct=="")
	{
		window.alert("Please! Enter your Contact");
		return false;
	}
	else
	{
	 	var isphone = /^(1\s|1|)?((\(\d{3}\))|\d{3})(\-|\s)?(\d{3})(\-|\s)?(\d{4})$/.test(cntct);
		if (!isphone)
		{
			window.alert("Please! Enter valid contact number");
			return false;
		}
	}

	if (address=="")
	{
		window.alert("Please! Enter your Address");
		return false;
	}
	if(bloodgroup==0)
	{
		window.alert("Please! Select Your Blood Group");
		return false;
	}
	if(usertype==0)
	{
		window.alert("Please! Select an User Type");
		return false;
	}
	if (pwrd1=="")
	{
		window.alert("Please! Enter your Password");
		return false;
	}

	if (rpwrd=="")
	{
		window.alert("Please! Re-Enter your Password");
		return false;
	}
	else if (rpwrd!=pwrd1)
	{
		window.alert("Password mismatched");
		return false;
	}
}