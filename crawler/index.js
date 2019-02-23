const xpath = require('xpath')
const dom = require('xmldom').DOMParser
const request = require('request')
const fs = require('fs');

const baseurl = 'http://pussintiristajat.blogspot.com';
const titleXpath="//*[@class='post-title entry-title']"
const bodyXpath="//*[@class='post-body entry-content']"
const postsXpath="//*[@class='posts']//@href"
const yearsXpath="//*[@class='hierarchy']//*[@class='hierarchy']//*[@class='post-count-link']//@href"
const contentDir = 'blog-posts';

fs.mkdir(contentDir, (err) => {
  if (err && err.code != 'EEXIST') {
    console.log(err);
    process.exit();
  }
});

function writeContentToFile(filename, title, body) {
  var writefile = contentDir + '/' + filename
  console.log('writing', writefile)
  fs.writeFileSync(writefile, title + '\n\n' + body);
}

function getTitle(content) {
  var doc = new dom().parseFromString(content);
  var titlestr = xpath.select("string("+titleXpath+")", doc);
  return titlestr.trim();
}

function getBody(content) {
  var doc = new dom().parseFromString(content);
  var body = xpath.select("string("+bodyXpath+")", doc);
  var bodyMod = body.trim().replace(/Published with Blogger-droid \S+/gi, '');
  return bodyMod;
}

function getBlogUrls(content) {
  var doc = new dom().parseFromString(content);
  var node = xpath.select(postsXpath, doc);
  blogUrls = []
  for (var i=0; i < node.length; i++) {
    blogUrls.push(node[i].value)
  }
  return blogUrls
}

function getYears(content) {
  var doc = new dom().parseFromString(content);
  var node = xpath.select(yearsXpath, doc);
  for (var i=0; i < node.length; i++) {
    getBlogs(node[i].value);
  }
}

function getBlogs(url) {
   request(url, (err, res, body) => {
     if (err) { return console.log(err); }
     var blogUrls = getBlogUrls(body);
     getContent(blogUrls)
   });
}

function getContent(urls) {
  for (var i=0; i < urls.length; i++) {
   request(urls[i], (err, res, body) => {
     if (err) { return console.log(err); }
     var title = getTitle(body);
     var body = getBody(body);
    var filename = res.request.path.replace(/\//g, '-').replace(/^-/, '').replace(/.html$/, '.txt');
     writeContentToFile(filename, title, body);
   });
  }
}

request(baseurl, (err, res, body) => {
  if (err) { return console.log(err); }
  getYears(body);
});
