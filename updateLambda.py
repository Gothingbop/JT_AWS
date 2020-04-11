"""
An example of how this package might be used to update a lambda function.
"""
from JT_AWS import Lambda_Client


def main():
    client = Lambda_Client(
        cred_path='./credentials.csv',
        bucket_name='jt-lambda-functions',
        region='us-east-2'
    )

    client.UpdateLambdaFromFolder(
        lambda_name='SubReport',
        folder_path='./Lambda'
    )


if __name__ == "__main__":
    main()
