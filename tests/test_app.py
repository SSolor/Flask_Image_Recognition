'''actual tests here'''

import numpy as np
import model

#homepage
def test_homepage_good(client):
    '''tests that the homepage can be reached properly'''
    res = client.get("/")
    assert res.status_code == 200


# valid request
def test_good_image(client):
    '''tests apropriate response from proper image'''
    with open("test_images/2/Sign 2 (87).jpeg","rb") as img:
        res = client.post("/prediction",
            data={"file":(img,"Sign 2 (87).jpeg")},
            content_type="multipart/form-data"
        )
    assert res.status_code==200
    assert b"2" in res.data

#invalid request
def test_invalid_method(client):
    '''tests that unallowed methods aren't allowed'''
    res = client.get("/prediction")
    assert res.status_code == 405

#missing file request
def test_missing_file(client):
    '''tests file missing'''
    res=client.post("/prediction",
        data={},
        content_type="multipart/form-data"
    )
    assert res.status_code==200
    #app never sends fail, it just tells users that it didn't work, but the page loads and all that
    assert b"File cannot be processed." in res.data

#not an image
def test_not_image(client):
    '''tests file that isn't image'''
    with open("test_images/notimage/text.txt","rb") as notimg:
        res = client.post("/prediction",
            data={"file":(notimg,"text.txt")},
            content_type="multipart/form-data"
        )
    assert res.status_code==200
    assert b"File cannot be processed." in res.data

#some edge cases
def test_image_badmetadata(client):
    '''tests file with weird header and metadata'''
    with open("test_images/2/Sign 2 (87).jpeg","rb") as img:
        res = client.post("/prediction",
            data={"file":(img,"Sign 2 (87).jpeg")},
            content_type="multipart/form-data",
            headers={"extra thigns that shoulnd't be here":"badinfo"}
        )
    assert res.status_code==200
    assert b"2" in res.data

#preprocessor
def test_preproc_valid():
    '''test that the preprocesor does what it should'''
    preprocced = model.preprocess_img("test_images/2/Sign 2 (97).jpeg")

    assert preprocced.shape == (1, 224, 224, 3)
    assert np.min(preprocced) >= 0 and np.max(preprocced) <= 1
    #size is good and values are normalized
