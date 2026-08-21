# Implementation Plan - Project Branding, Deployment, and Assets

Improve the project branding, prepare for Vercel deployment, and replace random photos with related content.

## User Review Required

> [!WARNING]
> **Database & Media on Vercel**: Vercel does not support persistent storage for SQLite (`db.sqlite3`) or local files (`media/`).
> - **Database**: Your posts will disappear after each deployment unless you connect an external PostgreSQL database (e.g., Neon.tech).
> - **Images**: Uploaded images will disappear. I recommend using [Cloudinary](https://cloudinary.com/) for Django media if you plan to keep the site on Vercel.

## Proposed Changes

### Branding & UI

#### [MODIFY] [base.html](file:///C:/Users/ahasa/Downloads/django_1-blog-main/django-blog-main/templates/base.html)
- Change header logo to "Habib Writes".
- Import "Dancing Script" or "Pacifico" from Google Fonts.
- Update CSS to apply the new font to the brand name.

### Deployment (Vercel)

#### [NEW] [vercel.json](file:///C:/Users/ahasa/Downloads/django_1-blog-main/django-blog-main/vercel.json)
- Configuration for Vercel to recognize the Django project using the Python runtime.

#### [MODIFY] [settings.py](file:///C:/Users/ahasa/Downloads/django_1-blog-main/django-blog-main/blog_main/settings.py)
- Add `whitenoise` for static file serving on Vercel.
- Configure `ALLOWED_HOSTS` for production.

### Content (Photos)

#### [NEW] [fix_images.py](file:///C:/Users/ahasa/Downloads/django_1-blog-main/django-blog-main/fix_images.py)
- A standalone script/management command to update existing blog posts with high-quality placeholder URLs from Unsplash based on categories (e.g., Tech, Lifestyle, Nature).

## Verification Plan

### Automated Tests
- Run `python manage.py check` to ensure settings are valid.

### Manual Verification
- View the local development server to see the new "Habib Writes" branding.
- Verify the `vercel.json` structure matches Vercel's requirements for Django.
