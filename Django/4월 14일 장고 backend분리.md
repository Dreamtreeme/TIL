### URL 및 HTTP request method 구성

댓글은 외래키를 사용해야하기 때문에 같은 주소를 쓸 수 없음

# 댓글의 전체 필드를 직렬화 하는 클래스
class CommentSerializer(serializers.ModelSerializer):
    # 외래 키 필드 article의 데이터를 재구성하기위한 도구
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title',)
    # 외래 키 필드인 article 의 데이터를 재구성
    article = ArticleTitleSerializer(read_only=True)




    class Meta:
        model = Comment
        fields = '__all__'
        # 외래키 필드를 유효성 검사 목록에서 빼줘야 함.
        # 그런데 응답 데이터에는 포함되어있어야 함 >>> 읽기 전용 필드로 설정
        # 유효성 검사는 외부로부터 들어온 데이터를 대상으로, 하지만 외래키는 사용자가 주는 것이 아닌 내부에서 자체적으로 생성되는 것임
        # read_only_fields = ('article', )

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    # 특정 댓글 데이터를 조회
    comment = Comment.objects.get(pk=comment_pk)


    if request.method == 'GET':
        # 조회한 단일 댓글 데이터를 가공
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 사용자가 보낸 새로운 댓글 데이터와 기존 데이터를 활용해 가공
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def comment_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글인지 단일 게시글을 조회
    article = Article.objects.get(pk=article_pk)
    # 사용자가 보낸 댓글 데이터를 활용해 가공
    serializer = CommentSerializer(data=request.data)
    # 유효한지 검사
    if serializer.is_valid(raise_exception=True):
        # 추가 데이터를 save 메서드의 인자로 작성
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


### Nested relationships 역참조 매니저 활용
# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):

    
    # comment_set에 활용할 댓글 데이터를 가공하는 도구
    class CommentDetailserializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
    # 기존에 있던 역참조 매니저인 comment_set의 값을 덮어쓰기
    comment_set = CommentDetailserializer(read_only = True, many=True)

    # 새로운 필드 생성
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    # SerializerMethodField의 값을 채울 함수
    # 이 함수는 반드시 get_<SerializerMethodField의 필드이름>으로 맞춰줘야 자동으로 호출됨
    def get_num_of_comments(self, obj):
        # 여기서 obj는 특정 게시글 인스턴스(3번 게시글이면 3번 객체,)
        # view 함수에서 annoate 해서 생긴 새로운 속성 결과를 사용할 수 있게됨
        return obj.num_of_comments


## drf-spectacular 라이브러리

1. pip install drf-spectacular 설치
2. INSTALLED_APPS 에 등록
    INSTALLED_APPS = [
    "drf_spectacular",
]
3. 관련 설정 코드 입력
    REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS' : 'drf_spectacular.openapi.AutoSchema'
}


