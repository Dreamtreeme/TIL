## AbstractUser

사용하는 이유: 더 많은 사용자 정보를 관리하고 싶다.

### choices 속성
사용자가 선택을 하도록 강제함.(표에서 선택하게 하는거,드롭다운형식)

### choices 사용법
from django.db import models

class MyModel(models.Model):
    STATUS_CHOICES = [
        ('draft', '임시 보관'),
        ('published', '게시됨'),
        ('rejected', '거부됨'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )

### MultipleChoiceField
from django import forms

class MyForm(forms.Form):
    FAVORITE_COLORS = [
        ('red', '빨간색'),
        ('green', '초록색'),
        ('blue', '파란색'),
        ('yellow', '노란색'),
    ]
    favorite_colors = forms.MultipleChoiceField(
        label='가장 좋아하는 색상을 선택하세요',
        choices=FAVORITE_COLORS,
        widget=forms.CheckboxSelectMultiple,  # 체크박스 형태로 표시
    )

    skills = forms.MultipleChoiceField(
        label='보유한 기술을 선택하세요',
        choices=[('python', 'Python'), ('django', 'Django'), ('javascript', 'JavaScript')],
        widget=forms.SelectMultiple,  # 드롭다운 목록 형태로 표시
    )

- MultipleChoiceField는 장고 폼에서 여러 개의 선택지를 제공하고 사용자가 그중 하나 또는 여러 개를 선택할 수 있도록 하는 강력한 필드 타입
- choices 속성을 통해 선택 옵션을 정의하고, widget 속성을 통해 사용자 인터페이스를 설정
- 폼 처리 시에는 선택된 값들이 리스트 형태로 제공

### cleaned_data

- Django Form 또는 ModelForm 내 유효성 검사 통과한 폼 데이터가 정리되어 저장되는 파이썬 dict 형태 객체.
- cleaned_data는 폼 유효성 검사(is_valid()) 성공 시에만 존재.
    - form.is_valid()가 True여야 cleaned_data 접근 가능.
- 검증 통과 값 저장 전 추가 로직 수행 필요 시 cleaned_data 활용 가능.