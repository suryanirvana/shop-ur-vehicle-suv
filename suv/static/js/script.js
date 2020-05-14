function articles() {
    const title = $('#id_title').val();
    const date = $('#id_date').val();
    const content = $('#id_content').val();
    var article = '{ "title":"' + title + '" , "date":"' + date + '" , "content":"' + content + '"}';
    var obj = JSON.parse(article);
    var article_stringify = JSON.stringify(obj);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var article = JSON.parse(this.responseText).article;
            for (var i = 0; i < article.length; i++) {
                $(".content").append(
                    '<div class="row articleBox">' +
                    '<h1 class="articleTitle" style="margin-left: 0; width: 100%;">' + article[i]['title'] + '</h1>' +
					'<h2 class="articleSubTitle" style="margin-left: 0; width: 100%;">' + article[i]['date'] + '</h2>' +
					'<p class="articleText">' + article[i]['content'] + '</p>'
                )
            }
        }
    }

    xhttp.open("POST", "api/articles/");
    xhttp.send(article_stringify);
}

function likearticles(i) {
    var id = '{ "id":"' + i + '"}';
    var obj = JSON.parse(id);
    var sendData = JSON.stringify(obj);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var like = JSON.parse(this.responseText).likeCount;
            $('#like'+i).html(like);
        }
    }
    xhttp.open("POST", "/api/likearticles/");
    xhttp.send(sendData);
}