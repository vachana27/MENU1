from django.http import HttpResponse

def about(request):
    return HttpResponse("""
<html>
<head>
<title>Login</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

<style>
body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    font-family:'Segoe UI',sans-serif;
    background:whitesmoke;
}

.login-box{
    width:380px;
    padding:45px;
    border-radius:25px;
    background:white;
    box-shadow:0 20px 40px rgba(0,0,0,0.25);
    animation:fadeIn 0.8s ease-in-out;
    background: linear-gradient(rgb(238, 129, 147),pink);
}

@keyframes fadeIn{
    from{opacity:0; transform:translateY(20px);}
    to{opacity:1; transform:translateY(0);}
}

.login-box h2{
    margin-bottom:5px;
    font-weight:700;
}

.subtitle{
    color:gray;
    margin-bottom:25px;
}

.input-group{
    margin-bottom:20px;
}

.input-group label{
    font-weight:600;
    font-size:14px;
}

.input-wrapper{
    position:relative;
}

.input-wrapper i{
    position:absolute;
    top:11px;
    left:12px;
    color:#764ba2;
}

.input-wrapper input{
    width:100%;
    padding:10px 10px 10px 38px;
    border-radius:12px;
    border:1px solid #ddd;
    outline:none;
    transition:0.3s;
}

.input-wrapper input:focus{
    border-color:#764ba2;
    box-shadow:0 0 6px rgba(118,75,162,0.4);
}

.btn-login{
    width:100%;
    padding:12px;
    border:none;
    border-radius:30px;
    background:linear-gradient(90deg,#667eea,#764ba2);
    color:white;
    font-weight:bold;
    font-size:16px;
    cursor:pointer;
    transition:0.3s;
}

.btn-login:hover{
    transform:scale(1.05);
    box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

.links{
    text-align:center;
    margin-top:15px;
    font-size:14px;
}

.links a{
    color:#764ba2;
    text-decoration:none;
    font-weight:600;
}
</style>
</head>

<body>

<div class="login-box">
    <h2>User Login</h2>
    <div class="subtitle">Please enter your details</div>

    <div class="input-group">
        <label>Email</label>
        <div class="input-wrapper">
            <i class="bi bi-person-fill"></i>
            <input type="text" placeholder="Enter email">
        </div>
    </div>

    <div class="input-group">
        <label>Password</label>
        <div class="input-wrapper">
            <i class="bi bi-lock-fill"></i>
            <input type="password" placeholder="Enter password">
        </div>
    </div>

    <button class="btn-login">Login</button>

    <div class="links">
        <a href="#">Forgot Password?</a><br>
        <a href="#">Register here</a>
    </div>
</div>

</body>
</html>
""")