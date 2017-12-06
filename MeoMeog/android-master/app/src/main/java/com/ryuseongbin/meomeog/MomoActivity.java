package com.ryuseongbin.meomeog;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

public class MomoActivity extends AppCompatActivity {
    private Button button_back;
    private Button button_go;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_momo);
        button_back = (Button) findViewById(R.id.bt_back);
        button_go = (Button) findViewById(R.id.bt_go);

        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MomoActivity.this,MainActivity.class);
                startActivity(intent);
            }
        });
        button_go.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                /*가는 길 찾기*/

            }
        });
    }
}
