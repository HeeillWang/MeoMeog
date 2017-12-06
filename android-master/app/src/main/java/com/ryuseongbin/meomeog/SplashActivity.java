package com.ryuseongbin.meomeog;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;

/**
 * Created by 민지 on 2017-12-05.
 */

public class SplashActivity extends Activity {
    protected  void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        try{
            Thread.sleep(2000);
        }catch(InterruptedException e){
            e.printStackTrace();
        }
        startActivity(new Intent(this, MainActivity.class ));
        finish();
    }
}
