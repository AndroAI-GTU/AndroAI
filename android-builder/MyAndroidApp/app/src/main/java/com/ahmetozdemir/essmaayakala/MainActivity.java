package com.ahmetozdemir.essmaayakala;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.os.Handler;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;

public class MainActivity extends AppCompatActivity
{
    Runnable runnable;
    Handler handler;
    int score; //Oyundaki skor değişkeni
    TextView timeText; //Uygulama içinde süreyi tutan metin kutusu
    TextView scoreText; //Uygulama içinde skoru tutan metin kutusu
    ImageView imageView3;
    ImageView imageView4;
    ImageView imageView5;
    ImageView imageView6;
    ImageView imageView7;
    ImageView imageView8;
    ImageView imageView9;
    ImageView imageView10;
    ImageView imageView11;

    ImageView [] imageArray;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //initialization
        timeText = findViewById(R.id.timeText);
        scoreText = findViewById(R.id.scoreText);
        imageView3 = findViewById(R.id.imageView3);
        imageView4 = findViewById(R.id.imageView4);
        imageView5 = findViewById(R.id.imageView5);
        imageView6 = findViewById(R.id.imageView6);
        imageView7 = findViewById(R.id.imageView7);
        imageView8 = findViewById(R.id.imageView8);
        imageView9 = findViewById(R.id.imageView9);
        imageView10 = findViewById(R.id.imageView10);
        imageView11 = findViewById(R.id.imageView11);

        imageArray = new ImageView[] {imageView3, imageView4, imageView5, imageView6, imageView7, imageView8, imageView9, imageView10, imageView11};

        hideImages();
        
        score = 0;

        //Uygulama açıldığı gibi geri sayım başlasın

        new CountDownTimer(10000, 1000) //Bir saniye 1000 milisaniye olur. Yani bu sayaç 10'dan geriye saniyede 1 sayar.
        {
            //Bu iki metod CountDownTimer'ın içinde kesinlikle her zaman olmalı!
            @Override
            public void onTick(long millisUntilFinished) //Her 1000 milisaniyede ne yapayım? Hangi saniyedeyiz = millisUntilFinished
            {
                timeText.setText(" Time : " + millisUntilFinished / 1000);
            }

            @Override
            public void onFinish() //Sayaç sona erdiğinde ne yapayım?
            {
                timeText.setText("Time is over!");
                handler.removeCallbacks(runnable); //runnable durdur

                //Süre bitince tüm görselleri sakla
                for (ImageView image: imageArray)
                {
                    image.setVisibility(View.INVISIBLE); //Görselleri sakla
                }

                AlertDialog.Builder alert = new AlertDialog.Builder(MainActivity.this);

                alert.setTitle("Restart Game");
                alert.setMessage("Are you sure restart game?");

                alert.setNegativeButton("Yes", new DialogInterface.OnClickListener()
                {
                    @Override
                    public void onClick(DialogInterface dialog, int which)
                    {
                        //restart (yani binevi aktiviteyi baştan başlatacağız)

                        Intent intent = getIntent();
                        finish();
                        startActivity(intent);
                    }
                });

                alert.setPositiveButton("No", new DialogInterface.OnClickListener()
                {
                    @Override
                    public void onClick(DialogInterface dialog, int which)
                    {
                        Toast.makeText(MainActivity.this, "Game Over!", Toast.LENGTH_SHORT).show();
                    }
                });

                alert.show();
            }
        }.start();
    }

    public void increaseScore (View view) //Fotoğrafa basınca skoru burada artırıyoruz
    {
        score++;

        scoreText.setText(" Score : " + score);
    }

    public void hideImages()
    {
        handler = new Handler();

        runnable = new Runnable()
        {
            @Override
            public void run()
            {
                for (ImageView image: imageArray)
                {
                    image.setVisibility(View.INVISIBLE); //Görselleri sakla
                }

                //Random classıyla oluşturulan sayıyı alıyoruz.
                Random random = new Random();
                int randNumber = random.nextInt(9); // 0-8 arası

                imageArray[randNumber].setVisibility(View.VISIBLE); //rastgele görsel çalıştır

                handler.postDelayed(runnable,250); //Her yarım saniye runnable ı çalıştır
                //handler.postDelayed(this,1000); bu şekilde de olabilir
            }
        };
        handler.post(runnable);
    }
}