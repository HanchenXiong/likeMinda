window.twttr = function (d, s, id) {
  var t, js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return; js = d.createElement(s); js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);
  return window.twttr || (t = { _e: [], ready: function (f) { t._e.push(f) } });
  }(document, 'script', 'twitter-wjs');

// When widget is ready, run masonry
twttr.ready(function (twttr) {
  twttr.events.bind('loaded', function (event) {
    $('.grid').masonry({
      itemSelector : '.grid-item',
      columnWidth : 300,
      gutter: 20
    });
  });
});

