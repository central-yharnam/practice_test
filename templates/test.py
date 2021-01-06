def loop():
  string="""<html>
    <head>
        <meta charset="utf-8">
        
        <style type="text/css">
            * {box-sizing: border-box;}
input[type=submit] {
    width: 20em;  height: 10em;
}
.wrapper {
    border: 2px solid #f76707;
    border-radius: 5px;
    background-color: #fff4e6;
}

.wrapper > div {
    border: 2px solid #ffa94d;
    border-radius: 5px;
    background-color: #ffd8a8;
    padding: 1em;
    color: #d9480f;
}
 .wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
}

        </style>
        
        <title>Practice test</title>
    </head>"""

  string += """<body>
  <form id="ptest" name='test' FORM method="POST">
  <h2>SAT TEST</h2>
  <div>
  <p>Test Number</p>
  <input type="text" id=testnum name=num>
  <p>Student ID</p>
  <input type="text" id=stid name=student>
  </div>
   """

  string += """


<h2>SECTION 1</h2>
<div class="wrapper">"""
  for i in range(0,52):
    #string += '''<form id="test" action="/login" method="POST" enctype="multipart/form-data">'''
    
    string += """
    
    <div>
    <p>Question {0}</p>
    <input type="radio" id={0}a name={0}a value="A">
    <label for="{0}a">A</label><br>

    <input type="radio" id={0}b name={0}b value="B">
    <label for="{0}b">B</label><br>

    <input type="radio" id={0}c name={0}c value="C">
    <label for="{0}c">C</label><br>

    <input type="radio" id={0}d name={0}d value="D">
    <label for="{0}d">D</label><br>
    </div>
  """.format(i+1)
  string += "</div>"

  string += """

<h2>SECTION 2</h2>
<div class="wrapper">"""
  for i in range(0,44):
    #string += '''<form id="test" action="/login" method="POST" enctype="multipart/form-data">'''
    
    string += """
    
    <div>
    <p>Question {0}</p>
    <input type="radio" id={1}a name={1}a value="A">
    <label for="{1}a">A</label><br>

    <input type="radio" id={1}b name={1}b value="B">
    <label for="{1}b">B</label><br>

    <input type="radio" id={1}c name={1}c value="C">
    <label for="{1}c">C</label><br>

    <input type="radio" id={1}d name={1}d value="D">
    <label for="{1}d">D</label><br>
    </div>
  """.format(i+1, i+1+52)

  string += "</div>"
  string += """


  <h2>SECTION 3</h2>
  <div class="wrapper">"""
  for i in range(0,15):
    #string += '''<form id="test" action="/login" method="POST" enctype="multipart/form-data">'''
    
    string += """
    
    <div>
    <p>Question {0}</p>
    <input type="radio" id={1}a name={1}a value="A">
    <label for="{1}a">A</label><br>

    <input type="radio" id={1}b name={1}b value="B">
    <label for="{1}b">B</label><br>

    <input type="radio" id={1}c name={1}c value="C">
    <label for="{1}c">C</label><br>

    <input type="radio" id={1}d name={1}d value="D">
    <label for="{1}d">D</label><br>
    </div>
  """.format(i+1, i+1+52+44)

  for i in range(15,20):
    string += """
      
      <div>
      <p>Question {0}</p>
      <input type="text" id={1}a name={1}a>
      </div>
    """.format(i+1, i+1+52+44)

  string += "</div>"
  string += """


  <h2>SECTION 4</h2>
  <div class="wrapper">"""
  for i in range(0,30):
    #string += '''<form id="test" action="/login" method="POST" enctype="multipart/form-data">'''
    
    string += """
    
    <div>
    <p>Question {0}</p>
    <input type="radio" id={1}a name={1}a value="A">
    <label for="{1}a">A</label><br>

    <input type="radio" id={1}b name={1}b value="B">
    <label for="{1}b">B</label><br>

    <input type="radio" id={1}c name={1}c value="C">
    <label for="{1}c">C</label><br>

    <input type="radio" id={1}d name={1}d value="D">
    <label for="{1}d">D</label><br>
    </div>
  """.format(i+1, i+1+52+44+20)



  for i in range(30,38):
    string += """
      
      <div>
      <p>Question {0}</p>
      <input type="text" id={1}a name={1}a>
      </div>
    """.format(i+1, i+1+52+44+20)

  string += "</div>"

    #string += '''<input type='button' value='Submit form' onclick='submitDetailsForm()' />'''
    #string += """<form action="{{ /login }}" method="post">
    #<input type="button" name="test">
    #<input type="submit">
    #</form>"""
  #string += """ <form action="" method="post">  <input type="submit" name = "test">"""
  '''string += """<form action="" method="post">
    <input type="text" name="test">
    <input type="submit">
</form>"""'''

  #string += ""
  string += """
  <input type="submit" value="Submit test" formaction="test/submit"></form>
  </div>"""
  return string