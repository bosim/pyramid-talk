import transaction

from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.renderers import render_to_response
from pyramid.url import route_url
from pyramid.view import view_config

from model import Article, DBSession


@view_config(route_name='article_list',
             renderer='templates/article_list.pt')
def article_list(request):
    results = []
    db_results = DBSession.query(Article).all()

    for db_result in db_results:
        results.append({
            'id': db_result.id,
            'url': route_url(
                'show_article',
                request,
                article=str(db_result.id)
            ),
            'title': db_result.title
        })

    return {
        'articles': results,
        'add_article': route_url('add_article', request)
    }


@view_config(route_name='show_article',
             renderer='templates/show_article.pt')
def show_article(context, request):
    article = {}
    db_result = DBSession.query(Article).filter(
        Article.id == context.article
    ).first()

    if not db_result:
        raise HTTPNotFound(
            "Article could not be found"
        )

    article['id'] = db_result.id
    article['title'] = db_result.title
    article['body'] = db_result.body

    return {
        'article': article,
        'back_url': route_url('article_list', request)
    }


@view_config(route_name='add_article')
def add_article(request):
    if 'form.submitted' in request.POST:
        with transaction.manager:
            article = Article(
                title=request.POST['title'],
                body=request.POST['body']
            )
            DBSession.add(article)

        return HTTPFound(
            location=route_url('article_list', request)
        )
    else:
        return render_to_response(
            'templates/add_article.pt',
            {'back_url': route_url('article_list', request)},
            request=request
        )
