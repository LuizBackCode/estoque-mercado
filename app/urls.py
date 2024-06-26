from django.contrib import admin
from django.urls import path
from contas.views import LoginView, RegistroView, LogoutView
from estoque.views import AdicionarProdutoView, ProdutosView, ProdutoDetailView, ProdutoUpdateView, ProdutoDeleteView, HomeView, FeedbackView, AdicionarFeedback, FeedbackDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('home/', HomeView.as_view(), name='home'),
    path('produtos/', ProdutosView.as_view(), name='produtos'),
    path('adicionar_produto', AdicionarProdutoView.as_view(), name='add_produto'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<int:pk>/editar_produto/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('produtos/<int:pk>/deletar_produto/', ProdutoDeleteView.as_view(), name='deletar_produto'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('add_feedback/', AdicionarFeedback.as_view(), name='add_feedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
