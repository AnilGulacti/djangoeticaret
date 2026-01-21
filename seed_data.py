import os
import django
import random
from django.utils.text import slugify

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangodm.settings.dev')
django.setup()

from django.contrib.auth import get_user_model
from products.models import Product, Thumbnail, CuratedProducts
from sellers.models import SellerAccount
from tags.models import Tag

User = get_user_model()

def create_sample_data():
    # 1. Create a superuser if it doesn't exist
    admin_user, created = User.objects.get_or_create(username='admin')
    if created:
        admin_user.set_password('admin123')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print("Superuser created: admin / admin123")
    else:
        print("Superuser already exists.")

    # 2. Create a Seller Account
    seller, created = SellerAccount.objects.get_or_create(user=admin_user)
    seller.active = True
    seller.save()
    print(f"Seller account ready for {admin_user.username}")

    # 3. Create some Tags
    tag_titles = ['Yazılım', 'Grafik', 'E-Kitap', 'Video', 'Ses']
    tags = []
    for title in tag_titles:
        tag, _ = Tag.objects.get_or_create(title=title)
        tags.append(tag)
    print("Tags created.")

    # 4. Create Sample Products
    products_data = [
        {
            'title': 'Gelişmiş E-Ticaret Teması',
            'description': 'Modern, hızlı ve SEO uyumlu bir e-ticaret teması. Tüm cihazlarla uyumludur.',
            'price': 499.99,
            'tags': ['Yazılım', 'Grafik']
        },
        {
            'title': 'Python ile Veri Analizi Eğitimi',
            'description': 'Sıfırdan uzmanlığa veri analizi yolculuğu. Pandas, Numpy ve Matplotlib içeriği ile.',
            'price': 199.50,
            'tags': ['E-Kitap', 'Yazılım']
        },
        {
            'title': 'Premium Logo Paketi',
            'description': '100+ farklı sektör için düzenlenebilir vektörel logo dosyaları.',
            'price': 75.00,
            'tags': ['Grafik']
        },
        {
            'title': 'Sinematik Ses Efektleri',
            'description': 'Projeleriniz için 500 adet yüksek kaliteli wav ses efekti.',
            'price': 29.90,
            'tags': ['Ses', 'Video']
        },
        {
            'title': 'Kurumsal Kimlik Rehberi',
            'description': 'Markanızın duruşunu belirleyen profesyonel bir rehber şablonu.',
            'price': 120.00,
            'tags': ['Grafik', 'E-Kitap']
        }
    ]

    for p_data in products_data:
        product, created = Product.objects.get_or_create(
            title=p_data['title'],
            defaults={
                'seller': seller,
                'description': p_data['description'],
                'price': p_data['price'],
                'sale_active': random.choice([True, False]),
                'sale_price': p_data['price'] * 0.8
            }
        )
        if created:
            # Add Tags
            for tag_title in p_data['tags']:
                tag = Tag.objects.get(title=tag_title)
                tag.products.add(product)
            print(f"Product created: {product.title}")

    # 5. Create a Curated Section
    curated, created = CuratedProducts.objects.get_or_create(
        user=admin_user,
        section_name='Haftanın Favorileri'
    )
    if created:
        selected_products = Product.objects.all()[:3]
        curated.products.add(*selected_products)
        print("Curated section 'Haftanın Favorileri' created.")

if __name__ == '__main__':
    create_sample_data()
    print("Sample data creation complete!")
