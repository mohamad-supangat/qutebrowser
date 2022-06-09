// ==UserScript==
// @name           Replace all reddit url
// @description    Convert all reddit.com url to libredd.it
// ==/UserScript==

var links, thisLink;
links = document.evaluate(
  "//a[@href]",
  document,
  null,
  XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
  null
);
for (var i = 0; i < links.snapshotLength; i++) {
  var thisLink = links.snapshotItem(i);
  // console.log(thisLink);

  thisLink.href = thisLink.href.replace(
    "https://www.reddit.com/",
    "https://libredd.it/"
  );
}
