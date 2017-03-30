# S3MultiPartUploader
uploads a file to s3 in multiparts, handles networ error/interruptions, assignment for indee tv interview

Indee-uploader
===========
#### Features:

* VERY resilient against upload interruptions. Even if your internet connection goes down, you accidentally close the browser or you want to continue the upload tomorrow, your upload progress is saved. Hell, it even works if you switch browsers or wifi connections!
* HTML5 - uses the `File`, `FileList`, and `Blob` objects
* Speed - it uses multiple workers for (potentially) four time increase in upload speed. E.g. on my computer I got 2.5-3 MB/s vs. < 1MB/s using only one worker. There is a tradeoff between upload speed and CPU consumption though.

#### Set up:

In order to use this library, you need the following:

* an Amazon S3 bucket where the files will get uploaded
* CORS settings allowing REST operations from your domain
* a separate, restricted user in Amazon IAM that can only access the upload bucket, and (VERY important!) can only create objects on the bucket, not delete them
* a backend that generates signatures, and optionally keeps track of uploaded chunks (for smart resume, e.g. after you refresh your browser)

1. You need to create an Amazon S3 bucket for uploads
2. You need to edit your Amazon S3 CORS configuration to allow communication from your domain. Here is what I use:

     ```xml
     <CORSRule>
         <AllowedOrigin>*</AllowedOrigin>
         <AllowedMethod>PUT</AllowedMethod>
         <AllowedMethod>POST</AllowedMethod>
         <AllowedMethod>GET</AllowedMethod>
         <AllowedMethod>HEAD</AllowedMethod>
         <MaxAgeSeconds>3000</MaxAgeSeconds>
         <AllowedHeader>*</AllowedHeader>
     </CORSRule>
     ```

3. You need to create a separate user in IAM


5. You need a backend to sign your REST requests (Flask + SQLAlchemy is used beacuse i wanted it to do it fast  example_backend.py. Migration to django would be simple transition of couple of functions alternative in django). 


6. For detailed instructions about how each of the ajax actions should respond, read the source code; there are two actions:
  * `signing_key` - returns a signature for authentication -- http://docs.aws.amazon.com/general/latest/gr/sigv4-calculate-signature.html . Also returns key/upload\_id/chunks if the file upload can be resumed. Should also return a backup\_key to be used in case that the first one is not usable.
  * `chunk_loaded` - (optional) notifies the server that a chunk has been uploaded; this is needed for browser-refresh resume (the backend will store the chunks in a database, and give the user the file key + upload id + chunks uploaded for the file to be uploaded)

#### How do I run the example locally?

1. Navigate to the project's root, e.g. `cd indeetv/indee`
2. Install requirements.txt: `sudo pip install -r requirements.txt`

3.You can see and modify these options in `settings.py` Give your secret key in settings.py.

4. Run `python example_backend.py`
5. Navigate to `http://localhost:8000/`
