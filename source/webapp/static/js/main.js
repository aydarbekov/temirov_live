$( document ).ready(function() {
    var anchors = document.getElementsByClassName('news-card');
    for(var i = 0; i < anchors.length; i++) {
        anchors[i].onclick = function() {
            s = this.children[0].getAttribute('newslink');
            title = this.getElementsByClassName('card-title');
            console.log(title[0].textContent);
            text = this.getElementsByClassName('card-text');
            main = document.getElementById('main-video');
            main.setAttribute('src', 'https://www.youtube.com/embed/' + s + '?;autoplay=1;');
            main_title = document.getElementById('main-title');
            main_text = document.getElementById('main-text');
            main_title.innerHTML = title[0].textContent;
            main_text.innerHTML = text[0].textContent;
            scrollTo(0, main.offsetTop - 100)
                }
            }
});
