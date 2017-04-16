#form.html
<html>
<head>
    <title>Please Sign In </title>
</head>
<body>
    {%s if message %}
    <p style="color.red"> {{message}}</p>
    {% endif %}
    <form action ="/signin" method="post">
    <ledend>Please sign in:</ledend>
    <p><input name="username" placeholer="Username" value="{{username}}"></p>
    <p><input name="password" placehoder="Password" type="password"></p>
    <p><button type="submit">Sign In> </button></p>
    </form>
</body>
</html>

