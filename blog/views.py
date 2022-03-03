from pydoc import render_doc
from django.shortcuts import render

# Dummy data - จำลองว่ามาจาก database
data = [
    {
        'title': 'Post 1',
        'author': 'Jome',
        'content': """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
    },
    {
        'title': 'Post 2',
        'author': 'Jome',
        'content': """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
    },
    {
    'title': 'Post 3',
    'author': 'Jome',
    'content': """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
},
    {
        'title': 'Post 4',
        'author': 'Jome',
        'content': """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
    },
]
# Create your views here.
def PostListView(request): 
    title = "Blog - Home"
    template = 'blog/home.html'
    # data_2col = list(zip(data[::2], data[1::2]))
    context = {
        'title': title,
        'posts': data,
        'posts_count': len(data)
    }
    return render(request, template, context)

def about(request):
    return render(request, 'blog/about.html')

def PostCreateView(request):
    title = "Blog - Create"
    template = 'blog/post_create.html'
    context = {
        'title': title,
    }
    return render(request, template, context)

def PostDetailView(request):
    title = "Blog - Detail"
    template = 'blog/post_detail.html'
    context = {
        'title': title,
    }
    return render(request, template, context)





