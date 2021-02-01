<!DOCTYPE html>
<html>
<head>
     <meta charset="utf-8">
     <style>
       header{
         border-bottom: 1px solid gray;
         padding: 20px;
       }
       nav{
         border-right: 1px solid gray;
         width: 200px;
         float: left;
         border-style: hidden;
       }
       article{
         float: left;
         padding-left: 20px;
         border-left: 1px solid gray;
       }
     </style>
</head>
<body>
	<header>
		<h1>
            LUNGNAHA
            <?php echo "go"; ?>
        </h1>
	</header>
	<nav>
        <ul>
    <?php 
        echo file_get_contents("list.html");
    ?>
        </ul>
    </nav>
    <article>
      <?php 
        if(id == 1){
            echo file_get_contents("one.html");
        }elseif(id == 2){
            echo file_get_contents("two.html");
        }elseif(id ==3){
            echo file_get_contents("three.html");
        }else{
            echo "저만의 비밀스러운 사이트에 오신걸 환영합니다.";
        }
      ?>
  </article>

</body>
</html>