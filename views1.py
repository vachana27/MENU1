from django.http import HttpResponse

def about(request):
    return HttpResponse("""
<head>  
    <title>My site</title>  <style>  
    body{  
        margin:0;  
        font-family: 'Segoe UI', sans-serif;  
        background: linear-gradient(to bottom, #0f1b4c, #1e90ff, #3ddc97);  
        height:100vh;  
    }  

    /* NAVBAR */  
    .navbar{  
        display:flex;  
        justify-content:space-between;  
        align-items:center;  
        padding:20px 60px;  
        background: linear-gradient(to right, #2b6cb0, #38b2ac);  
    }  

    .logo{  
        color:white;  
        font-size:32px;  
        font-weight:bold;  
    }  

    .nav-links{  
        display:flex;  
        align-items:center;  
    }  

    .nav-links a{  
        color:white;  
        text-decoration:none;  
        margin:0 20px;  
        font-size:20px;  
        position:relative;  
        padding-bottom:5px;  
        transition:0.3s;  
    }  

    /* Yellow underline animation */  
    .nav-links a::after{  
        content:"";  
        position:absolute;  
        width:0%;  
        height:3px;  
        left:0;  
        bottom:0;  
        background:gold;  
        transition:0.3s;  
    }  

    .nav-links a:hover{  
        color:#ffe066;  
    }  

    .nav-links a:hover::after{  
        width:100%;  
    }  

    /* Dropdown */  
    .dropdown{  
        position:relative;  
    }  

    .dropdown-content{  
        display:none;  
        position:absolute;  
        top:50px;  
        left:0;  
        background:#f0f0f0;  
        width:260px;  
        border-radius:20px;  
        padding:15px 0;  
        box-shadow:0 10px 30px rgba(0,0,0,0.2);  
    }  

    .dropdown-content a{  
        display:block;  
        padding:15px 25px;  
        margin:8px 20px;  
        border-radius:12px;  
        color:#333;  
        font-size:22px;  
    }  

    .dropdown-content a:hover{  
        background:linear-gradient(to right,#3182ce,#63b3ed);  
        color:white;  
    }  

    .dropdown:hover .dropdown-content{  
        display:block;  
    }  

    /* Login Button */  
    .btn-login{  
        background:#e2e8f0;  
        color:#2b6cb0 !important;  
        padding:10px 25px;  
        border-radius:30px;  
        font-weight:bold;  
    }  

    .btn-login:hover{  
        background:white;  
    }  
</style>

</head>  <body>  <div class="navbar">  
    <div class="logo">MENU</div>  

    <div class="nav-links">  
        <a href="#">Home</a>  
        <a href="#">About </a>  

        <div class="dropdown">  
            <a href="#">Courses ▾</a>  
            <div class="dropdown-content">  
                <a href="#">Python</a>  
                <a href="#">Django</a>  
                <a href="#">Web Development</a>  
            </div>  
        </div>  

        <a href="#">Contact</a>  
        <a href="#" class="btn-login">Login</a>  
    </div>  
</div>

</body>  
</html>
""")

def course(request):
    return HttpResponse("Welcome to courses")

def courseDetails(request, cname):
    return HttpResponse(cname)
