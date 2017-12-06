package com.ryuseongbin.meomeog;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

/**
 * Created by 민지 on 2017-12-05.
 */

public class Recommend extends AppCompatActivity {
    private Button button_back;
    private Button button_go;
    private Button button5;
    private Button button6;
    private Button button7;
    Intent intent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommend);
        button_back = (Button) findViewById(R.id.bt_back);
        button_go = (Button) findViewById(R.id.bt_go);
        button5 = (Button) findViewById(R.id.button5);
        button6 = (Button) findViewById(R.id.button6);
        button7 = (Button) findViewById(R.id.button7);

        intent = new Intent(Recommend.this,MomoActivity.class);



        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                intent.putExtra("name","첫번째식당");
                intent.putExtra("category","한식");
                intent.putExtra("grade","4.2");

                startActivity(intent);
            }
        });
        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                intent.putExtra("name","두번째식당");
                intent.putExtra("category","일식");
                intent.putExtra("grade","3.7");
                startActivity(intent);
            }
        });
        button7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                intent.putExtra("name","세번째식당");
                intent.putExtra("category","중식");
                intent.putExtra("grade","2.7");
                startActivity(intent);
            }
        });




        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        button_go.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                /*다시 추천*/

            }
        });
    }
}
