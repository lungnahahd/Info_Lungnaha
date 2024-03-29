# Info_Lungnaha
Make my own Blog with Django
------------------------------------
### 블로그 생성 내용
  * Django를 통해서 블로그 생성
  * 웹 템플릿은 오픈소스를 사용
  * DB로는 Mysql을 연동을 통해서 사용
  * 글 작성 방법은 admin 사이트에 접속하거나 Authenticate 페이지에 접속해서 admin 계정 권한을 얻어야만 작성 가능
      * 글 수정이나 삭제도 해당 권한을 얻어야 수행 가능
  * 글 작성으로는 Ckeditor를 사용해서 이미지와 글을 함께 업로드 가능
  * Cloudinary를 통해 이미지를 서버에 저장(Saas)
  * 배포는 Heroku를 통해서 배포 진행(Paas)
----------------------------------
### 블로그 설명
  * Home
      * 현재 작성된 글 리스트를 확인 가능
      * 글 리스트의 Open 버튼을 누르면 전체 내용을 확인 가능하고 이에 따른 댓글을 달 수 있음
  * About
      * 나에 대한 전반적인 이력과 나에게 contact을 할 수 있는 방법에 대해 작성
  * Post
      * 글을 작성할 수 있는 페이지이지만, admin 권한을 얻지 못하면 글 작성 불가
  * Authenticate
      * admin 계정의 권한을 얻거나 해당 권한을 로그아웃 할 수 있는 페이지
----------------------------
### 개선 필요 내용
  * Heroku는 이미지를 서버에 저장하는 형식이 아니라서 서버가 sleep 상태에 들어가면 이미지가 누락되는 현상 발생
      * 이는 Cloudinary 나 S3의 연동을 통해서 추후에 해결할 예정
  * Post와 Authenticate 페이지의 디자인 측면이 취약한데 이는 추후에 보강할 예정
---------------------
### 느낀 점
먼저 이렇게 간단해 보이는 블로그도 정말 많은 기능이 있다는 것을 새삼 느끼게 되었고, 아무리 간단한 블로그 이지만 내 힘으로 처음 만든 블로그이고 드디어 만들었다는 사실에 내 자신이 뿌듯했다.
그리고 공부를 하면서 만들어 가는 과정을 통해서 정말 글로만 배우는 것이 아니라 직접 기능을 추가하면서 몸으로 크게 와닿는 학습을 한 것 같다. 그리고 만드는 것이 끝이 아니라 배포하는 과정에서도
많은 시간과 노력이 걸린 것을 통해 배포의 중요성과 어려움도 알게 되었다.
----------------------
![스크린샷(27)](https://user-images.githubusercontent.com/67555400/110235377-095d2d00-7f73-11eb-855a-b4310117caa3.png)
![스크린샷(28)](https://user-images.githubusercontent.com/67555400/110235389-17ab4900-7f73-11eb-99dc-a9babd2648bc.png)
![스크린샷(29)](https://user-images.githubusercontent.com/67555400/110235399-2134b100-7f73-11eb-8929-1380fdb0b32f.png)
