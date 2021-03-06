html_exercise="""<!DOCTYPE html>
<!-- saved from url=(0026)https://docs.python.org/3/ -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>3.8.4 Documentation</title>
    <link rel="stylesheet" href="./3.8.4 Documentation_files/pydoctheme.css" type="text/css">
    <link rel="stylesheet" href="./3.8.4 Documentation_files/pygments.css" type="text/css">
    
    <script type="text/javascript" id="documentation_options" data-url_root="./" src="./3.8.4 Documentation_files/documentation_options.js.下载"></script>
    <script type="text/javascript" src="./3.8.4 Documentation_files/jquery.js.下载"></script>
    <script type="text/javascript" src="./3.8.4 Documentation_files/underscore.js.下载"></script>
    <script type="text/javascript" src="./3.8.4 Documentation_files/doctools.js.下载"></script>
    <script type="text/javascript" src="./3.8.4 Documentation_files/language_data.js.下载"></script>
    
    <script type="text/javascript" src="./3.8.4 Documentation_files/sidebar.js.下载"></script>
    
    <link rel="search" type="application/opensearchdescription+xml" title="Search within Python 3.8.4 documentation" href="https://docs.python.org/3/_static/opensearch.xml">
    <link rel="author" title="About these documents" href="https://docs.python.org/3/about.html">
    <link rel="index" title="Index" href="https://docs.python.org/3/genindex.html">
    <link rel="search" title="Search" href="https://docs.python.org/3/search.html">
    <link rel="copyright" title="Copyright" href="https://docs.python.org/3/copyright.html">
    <link rel="canonical" href="https://docs.python.org/3/index.html">
    
      
      
    

    
    <style>
      @media only screen {
        table.full-width-table {
            width: 100%;
        }
      }
    </style>

    <link rel="shortcut icon" type="image/png" href="./3.8.4 Documentation_files/py.png">
    
    <script type="text/javascript" src="./3.8.4 Documentation_files/copybutton.js.下载"></script>
    
     


  </head><body>
  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="https://docs.python.org/3/genindex.html" title="General Index" accesskey="I">index</a></li>
        <li class="right">
          <a href="https://docs.python.org/3/py-modindex.html" title="Python Module Index">modules</a> |</li>

    <li><img src="./3.8.4 Documentation_files/py.png" alt="" style="vertical-align: middle; margin-top: -1px"></li>
    <li><a href="https://www.python.org/">Python</a> »</li>
    

    <li><span class="language_switcher_placeholder"><select><option value="en" selected="selected">English</option><option value="es">Spanish</option><option value="fr">French</option><option value="ja">Japanese</option><option value="ko">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="zh-cn">Simplified Chinese</option><option value="zh-tw">Traditional Chinese</option></select></span> <span class="version_switcher_placeholder"><select><option value="3.10">dev (3.10)</option><option value="3.9">pre (3.9)</option><option value="3.8" selected="selected">3.8.4</option><option value="3.7">3.7</option><option value="3.6">3.6</option><option value="3.5">3.5</option><option value="2.7">2.7</option></select></span> <a href="https://docs.python.org/index.html">Documentation</a> »</li>

    <li class="right">
        

    <div class="inline-search" style="" role="search">
        <form class="inline-search" action="https://docs.python.org/3/search.html" method="get">
          <input placeholder="Quick search" type="text" name="q">
          <input type="submit" value="Go">
          <input type="hidden" name="check_keywords" value="yes">
          <input type="hidden" name="area" value="default">
        </form>
    </div>
    <script type="text/javascript">$('.inline-search').show(0);</script>
         |
    </li>

      </ul>
    </div>    

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <h1>Python 3.8.4 documentation</h1>
  <p>
  Welcome! This is the documentation for Python 3.8.4.
  </p>
  <p><strong>Parts of the documentation:</strong></p>
  <table class="contentstable" align="center"><tbody><tr>
    <td width="50%">
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/whatsnew/3.8.html">What's new in Python 3.8?</a><br>
        <span class="linkdescr"> or <a href="https://docs.python.org/3/whatsnew/index.html">all "What's new" documents</a> since 2.0</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/tutorial/index.html">Tutorial</a><br>
         <span class="linkdescr">start here</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/library/index.html">Library Reference</a><br>
         <span class="linkdescr">keep this under your pillow</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/reference/index.html">Language Reference</a><br>
         <span class="linkdescr">describes syntax and language elements</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/using/index.html">Python Setup and Usage</a><br>
         <span class="linkdescr">how to use Python on different platforms</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/howto/index.html">Python HOWTOs</a><br>
         <span class="linkdescr">in-depth documents on specific topics</span></p>
    </td><td width="50%">
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/installing/index.html">Installing Python Modules</a><br>
         <span class="linkdescr">installing from the Python Package Index &amp; other sources</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/distributing/index.html">Distributing Python Modules</a><br>
         <span class="linkdescr">publishing modules for installation by others</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/extending/index.html">Extending and Embedding</a><br>
         <span class="linkdescr">tutorial for C/C++ programmers</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/c-api/index.html">Python/C API</a><br>
         <span class="linkdescr">reference for C/C++ programmers</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/faq/index.html">FAQs</a><br>
         <span class="linkdescr">frequently asked questions (with answers!)</span></p>
    </td></tr>
  </tbody></table>

  <p><strong>Indices and tables:</strong></p>
  <table class="contentstable" align="center"><tbody><tr>
    <td width="50%">
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/py-modindex.html">Global Module Index</a><br>
         <span class="linkdescr">quick access to all modules</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/genindex.html">General Index</a><br>
         <span class="linkdescr">all functions, classes, terms</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/glossary.html">Glossary</a><br>
         <span class="linkdescr">the most important terms explained</span></p>
    </td><td width="50%">
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/search.html">Search page</a><br>
         <span class="linkdescr">search this documentation</span></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/contents.html">Complete Table of Contents</a><br>
         <span class="linkdescr">lists all sections and subsections</span></p>
    </td></tr>
  </tbody></table>

  <p><strong>Meta information:</strong></p>
  <table class="contentstable" align="center"><tbody><tr>
    <td width="50%">
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/bugs.html">Reporting bugs</a></p>
      <p class="biglink"><a class="biglink" href="https://devguide.python.org/docquality/#helping-with-documentation">Contributing to Docs</a></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/about.html">About the documentation</a></p>
    </td><td width="50%">
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/license.html">History and License of Python</a></p>
      <p class="biglink"><a class="biglink" href="https://docs.python.org/3/copyright.html">Copyright</a></p>
    </td></tr>
  </tbody></table>

          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper" style="float: left; margin-right: 0px; width: 202px; top: 0px;"><h3>Download</h3>
<p><a href="https://docs.python.org/3/download.html">Download these documents</a></p>
<h3>Docs by version</h3>
<ul>
  <li><a href="https://docs.python.org/3.10/">Python 3.10 (in development)</a></li>
<li><a href="https://docs.python.org/3.9/">Python 3.9 (pre-release)</a></li>
<li><a href="https://docs.python.org/3.8/">Python 3.8 (stable)</a></li>
<li><a href="https://docs.python.org/3.7/">Python 3.7 (security-fixes)</a></li>
<li><a href="https://docs.python.org/3.6/">Python 3.6 (security-fixes)</a></li>
<li><a href="https://docs.python.org/3.5/">Python 3.5 (security-fixes)</a></li>
<li><a href="https://docs.python.org/2.7/">Python 2.7 (EOL)</a></li>
  <li><a href="https://www.python.org/doc/versions/">All versions</a></li>
</ul>

<h3>Other resources</h3>
<ul>
  
  <li><a href="https://www.python.org/dev/peps/">PEP Index</a></li>
  <li><a href="https://wiki.python.org/moin/BeginnersGuide">Beginner's Guide</a></li>
  <li><a href="https://wiki.python.org/moin/PythonBooks">Book List</a></li>
  <li><a href="https://www.python.org/doc/av/">Audio/Visual Talks</a></li>
  <li><a href="https://devguide.python.org/">Python Developer’s Guide</a></li>
</ul>
        </div>
      <div id="sidebarbutton" title="Collapse sidebar" style="border-radius: 0px 5px 5px 0px; color: rgb(68, 68, 68); background-color: rgb(204, 204, 204); font-size: 1.2em; cursor: pointer; height: 945.6px; padding-top: 1px; padding-left: 1px; margin-left: 218px;"><span style="display: block; position: fixed; top: 257px;">«</span></div></div>
      <div class="clearer"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="https://docs.python.org/3/genindex.html" title="General Index">index</a></li>
        <li class="right">
          <a href="https://docs.python.org/3/py-modindex.html" title="Python Module Index">modules</a> |</li>

    <li><img src="./3.8.4 Documentation_files/py.png" alt="" style="vertical-align: middle; margin-top: -1px"></li>
    <li><a href="https://www.python.org/">Python</a> »</li>
    

    <li>
      <a href="https://docs.python.org/3/#">3.8.4 Documentation</a> »
    </li>

    <li class="right">
        

    <div class="inline-search" style="" role="search">
        <form class="inline-search" action="https://docs.python.org/3/search.html" method="get">
          <input placeholder="Quick search" type="text" name="q">
          <input type="submit" value="Go">
          <input type="hidden" name="check_keywords" value="yes">
          <input type="hidden" name="area" value="default">
        </form>
    </div>
    <script type="text/javascript">$('.inline-search').show(0);</script>
         |
    </li>

      </ul>
    </div>  
    <div class="footer">
    © <a href="https://docs.python.org/3/copyright.html">Copyright</a> 2001-2020, Python Software Foundation.
    <br>

    The Python Software Foundation is a non-profit corporation.
<a href="https://www.python.org/psf/donations/">Please donate.</a>
<br>
    <br>

    Last updated on Jul 18, 2020.
    <a href="https://docs.python.org/3/bugs.html">Found a bug</a>?
    <br>

    Created using <a href="https://www.sphinx-doc.org/">Sphinx</a> 2.3.1.
    </div>

    <script type="text/javascript" src="./3.8.4 Documentation_files/switchers.js.下载"></script>
  
</body></html>
"""