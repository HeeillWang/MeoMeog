package com.ryuseongbin.meomeog;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MomoActivity extends AppCompatActivity {
    private Button button_back;
    private Button button_go;
    private TextView t1, t2, t3;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_momo);

        final Intent intent = getIntent();
        String name = intent.getStringExtra("name");
        String category = intent.getStringExtra("category");
        String grade = intent.getStringExtra("grade");


        t1 = (TextView)findViewById(R.id.t1);
        t2 = (TextView)findViewById(R.id.textView1);
        t3 = (TextView)findViewById(R.id.textView2);
        t1.setText(name);
        t2.setText(t2.getText() + " "+category);
        t3.setText(t3.getText() + " "+grade);


        button_back = (Button) findViewById(R.id.bt_back);
        button_go = (Button) findViewById(R.id.bt_go);

        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        button_go.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getApplicationContext(), "아직 개발 중 입니다.", Toast.LENGTH_LONG).show();
            }
        });
    }
}
