import io
import gzip

csv_content = "name,age\nAlice,30\nBob,25"
text_stream = io.StringIO(csv_content)
csv_bytes = text_stream.getvalue().encode('utf-8')
compressed_stream = io.BytesIO()
with gzip.GzipFile(fileobj=compressed_stream, mode='wb') as gz_file:
    gz_file.write(csv_bytes)
compressed_data = compressed_stream.getvalue()

decompressed_stream = io.BytesIO(compressed_data)
with gzip.GzipFile(fileobj=decompressed_stream, mode='rb') as gz_file:
    decompressed_bytes = gz_file.read()

decompressed_text = decompressed_bytes.decode('utf-8')
result_stream = io.StringIO(decompressed_text)


print("Decompressed CSV content:")
for line in result_stream:
    print(line.strip())
